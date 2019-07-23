import socket
import threading
import random
import time
import re
import inspect


SERVER = ('localhost', 8080) 
TRACE = True #activate trace

def trace(func):
	"""Tracing wrapper
	
	Args:
		func (function): function to trace

	Returns:
		'callf' function if LOGGING True
		otherwise returns func

	"""
	if TRACE:
		trace = open('logs/trace.log', 'a+')
		def callf(*args, **kwargs):
			"""Trace
			Writes in file info about called function

			Returns:
				func result
			"""
			trace.write(f'Call func {func.__name__}({args} / {kwargs}) from {inspect.stack()[1][-3]} function\n')
			returns = func(*args, **kwargs)
			trace.write(f'Returns {returns}\n\n')
			return returns

		return callf

	else:
		return func


class Client:
	def __init__(self, name, server):
		"""A client class

		Args:
			name (str): name of the client
			server (tuple): (ip, port) of a chat server to connect

		Attributes:
			id (int): ID of the client
			s (socket): socket of the client
			rT (thread): receiving thread
		"""
		self.name = name
		self.server = server
		self.id = random.randint(100, 999)
		self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.rT = threading.Thread(target=self.receiving, name='ReceiveThread')

	@trace
	def run(self):
		"""Begins the main loop
		establishing connection with the server and waiting for the user's input
		(there two threads: first for sending, second for receiving)
		"""
		self.shutdown = False
		self.s.connect(('localhost', 0))
		self.sendjson('enter', None, self.server)
		self.rT.start()

		while not self.shutdown:
			try:
				message = input('')

				#распознаем команды 
				if re.match(r'/pm \d\d\d', message) is not None:
					self.sendjson('pmmsg', message[4:], self.server)

				elif re.match(r'/exit', message) is not None:
					self.sendjson('exit', None, self.server)
					print('\n///exit///')
					self.shutdown = True
					break

				elif re.match(r'/help', message) is not None:
					self.sendjson('help', None, self.server)

				elif re.match(r'/getonline', message) is not None:
					self.sendjson('getonline', None, self.server)

				elif re.match(r'/\w', message) is not None: #неизвестная команда
					print('Unknown command. Type "/help" for redeem a list of all commands')

				elif message != '': #если сообщение не пустое и не явлсяется командой
					self.sendjson('msg', message, self.server)

			except Exception as ex:
				print('Error in sending:\t', ex)
				self.shutdown = True
				break

		self.rT.join()
		self.s.close()

	@trace
	def sendjson(self, action, msg, addr):
		"""Packing data in json format for server and sending to a recipient

		Args:
			action (str): one of these - (enter, msg, pmmsg, exit)
			msg (str): user message
			addr (str): IPv4 address of the recipient
		"""
		#пришлось в такую длинную строку вынести
		#т.к. тройные кавычки работали некорректно, а перенос слешэм вызывал ошибку c форматированной строкой
		return self.s.sendto(('{'+f'"action":"{action}",\n"time":"{time.strftime("%H:%M:%S")}",\n"message":"{msg}",\n"user":["{self.name}", {self.id}]'+'}').encode('utf-8'), addr)

	@trace
	def receiving(self):
		"""Receive thread

		Waiting for message from connected users and then outputs it
		"""
		while not self.shutdown:
			try:
				time.sleep(0.1) #для избежания гонки
				data, addr = self.s.recvfrom(1024)
				data = data.decode('utf-8')
				flag = '>>>' not in data #костыль, который сделан только ради более-менее красивого вывода
				print(data, end='\n'*flag)

			except Exception as ex:
				print('Error in receiving:\t', ex)
				self.shutdown = True
				return

if __name__ == '__main__':
	name = input('Name: ')
	client = Client(name, SERVER)
	client.run()