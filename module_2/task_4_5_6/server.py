import socket
import time
import json
import sys

"""UDPServer

Constants:
	SERVER (tuple): tuple of IP and PORT data
	TIMEOUT (float): time in seconds how long to wait for a request
	LOGGING (bool): if True, sys.stdout changes to writing in log file; controls functions calls

"""

SERVER = ('localhost', 8080)
TIMEOUT = 60.0
LOGGING = False

if LOGGING:
	sys.stdout = open('logs/server.log', 'a+') #сохраняем весь вывод сервера

clients = {} #база клиентов

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(TIMEOUT) #таймаут чтобы хост мог самовольно ликвидироваться если его не используют
s.bind(SERVER)

help_info = 'Chat commands:\n\n/pm ID MESSAGE - write personal MESSAGE to the user with ID\n'
help_info += '/exit - leave chat\n/getonline - get online ids\n/help - get commands\n'

print('\n[ Server Started ]\n')

while True:
	try:
		data, addr = s.recvfrom(1024)
		data = json.loads(data.decode('utf-8'), encoding='utf-8') #преобразуем str в json

		#уведомление отправителю об успешном получении его сообщения
		s.sendto(('\n>>> successfully received [202]\n\n').encode('utf-8'), addr)

		print(data) #добавление лога

		#добавление юзера в базу и приветствие
		if data['action'] == 'enter':
			clients[data['user'][1]] = addr
			for client in clients.values():
				if client != addr: #отправляем всем, кроме отправителя
					s.sendto((f'[ {data["user"][0]} #{data["user"][1]} ] ==> join chat').encode('utf-8'), client)
				else: #отправляем список доступных команд
					s.sendto(help_info.encode('utf-8'), addr)

		#сообщение предназначено всем
		elif data['action'] == 'msg':
			for client in clients.values():
				if client != addr:
					s.sendto((f'[ {data["user"][0]} #{data["user"][1]} ] :: {data["message"]}').encode('utf-8'), client)

		#сообщение предназначено определенному юзеру
		elif data['action'] == 'pmmsg':
			if int(data['message'][:3]) in clients.keys():
				s.sendto((f'[ {data["user"][0]} #{data["user"][1]} ] //PM// :: {data["message"][4:]}').encode('utf-8'), clients[int(data['message'][:3])])
			else:
				s.sendto((f'\n>>> unknown user id {data["message"][:3]} [404]\n\n').encode('utf-8'), addr)

		#удаление юзера из базы при его выходе в оффлайн
		elif data['action'] == 'exit':
			if data['user'][1] in clients.keys():
				del clients[data['user'][1]]
			else:
				s.sendto((f'[ {data["user"][0]} #{data["user"][1]} ] <== left chat').encode("utf-8"), addr)

		#выводит список онлайна в формате ID
		elif data['action'] == 'getonline':
			s.sendto((f'Currently online: \n\t{list(clients.keys())}').encode('utf-8'), addr)

		#выводит список доступных команд
		elif data['action'] == 'help':
			s.sendto(help_info.encode('utf-8'), addr)
	
		#неизвестное действие
		else:
			s.sendto((f'\n>>> unknown action type {data["action"]} [400]\n\n').encode('utf-8'), addr)

	except Exception as ex:
		print('\n', ex)
		print('\n[ Server Stoped ]\n' + '-'*90)
		break

s.close()