import threading
import random
from time import sleep


def write(n):
	global flag, count, book

	while (random.random()<0.8 and flag) or count==0: #шанс 20% что писатели сочтут книгу дописанной
		wrt.acquire()
		count += 1
		write_time = random.randint(1, 5)
		sleep(write_time)
		book += str(n)
		print(f'\nThe writer #{n} wrote a new part in {write_time} seconds!\n')
		wrt.release()
		sleep(0.5)
		lock.set()

	flag = False
	print(f'WRITING STOPED, TOTAL PARTS: {count}\nBOOK: {book}\n')

def read(n):
	global flag, book

	while flag:
		lock.wait()
		author = book[-1]
		print(f'The reader #{n} read a new part! Author: {author}')
		sleep(0.1)
		lock.clear()

readers = random.randint(3, 10)
writers = 2
book = ''

print('TOTAL READERS NUMBER: ', readers)

lock = threading.Event()
wrt = threading.Lock()
flag = True
count = 0

for i in range(readers):
	threading.Thread(target=read, args=(i,)).start()

for i in range(writers):
	t = threading.Thread(target=write, args=(i,))
	t.daemon = True
	t.start()
