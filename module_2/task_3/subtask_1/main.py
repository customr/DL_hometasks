import threading
import random
from time import sleep


def write(n):
	global flag

	while random.random()<0.8 and flag: #шанс 20% что писатели сочтут книгу дописанной
		wrt.acquire()
		write_time = random.randint(1, 5)
		sleep(write_time) 
		print(f'\nThe writer #{n} wrote a new part in {write_time} seconds!\n')
		wrt.release()
		sleep(0.5)
		lock.set()

	flag = False
	print('WRITING STOPED\n')

def read(n):
	global flag

	while flag:
		lock.wait()
		sleep(0.05 * n)
		print(f'The reader #{n} read a new part!')
		lock.clear()

readers = random.randint(3, 10)
writers = 2

print('TOTAL READERS NUMBER: ', readers)

lock = threading.Event()
wrt = threading.Lock()
flag = True

for i in range(readers):
	t = threading.Thread(target=read, args=(i,))
	t.start()

for i in range(writers):
	t = threading.Thread(target=write, args=(i,))
	t.daemon = True
	t.start()
