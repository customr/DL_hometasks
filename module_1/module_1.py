class Company:
	def __init__(self, name, address, check_acc, dep_list=[]):
		assert isinstance(name, str), 'wrong company name!'
		assert isinstance(check_acc, int), 'check account must contain only numbers'
		assert isinstance(dep_list, list), 'departament list gone wrong'

		self.name = name
		self.address = address
		self.check_acc = check_acc
		self.dep_list = dep_list

	def __getitem__(self, key):
		for dep in self.dep_list:
			if dep.id==key:
				return dep

	def __str__(self):
		return f'{self.name} departaments: {[dep.name for dep in self.dep_list]}'

	def add_depart(self, *args, **kwargs):
		self.dep_list.append(Departament(*args, **kwargs))

	def get_poor_workers(self):
		assert len(self.dep_list) != 0, f'no one departament in {self.name} company'

		medium_salary = {}
		for dep in self.dep_list:
			assert len(dep.workers_list) != 0, f'no one worker in {dep.name} departament'

			counter = 0.0
			for n, worker in enumerate(dep.workers_list):
				if worker.position != 'CEO':
					counter += worker.salary

			medium_salary[f'{dep.name}'] = counter / n

		poor_workers = []
		for worker in dep.workers_list:
			if worker.salary < medium_salary[dep.name]:
				poor_workers.append(worker)

		return print(f'Poor workers in {dep.name} departament: \n{poor_workers}')

	def get_ceo(self):
		assert len(self.dep_list) != 0, f'no one departament in {self.name} company'

		dep_ceo = {}

		for dep in self.dep_list:
			assert len(dep.workers_list) != 0, f'no one worker in {dep.name} departament'
			for worker in dep.workers_list:
				if worker.position == 'CEO':
					dep_ceo[f'{dep.name}'] = worker

		return dep_ceo

	def get_kids(self):
		assert len(self.dep_list) != 0, f'no one departament in {self.name} company'

		workers_kids = {}

		for dep in self.dep_list:
			assert len(dep.workers_list) != 0, f'no one worker in {dep.name} departament'
			for worker in dep.workers_list:
				if len(worker.kids)!=0:
					for kid in worker.kids:
						if not kid.adult:
							try:
								workers_kids[f'{worker.first_name} {worker.last_name} KID(S)'].append(kid)
							except Exception:
								workers_kids[f'{worker.first_name} {worker.last_name} KID(S)'] = [kid]

		return workers_kids

class Departament:
	def __init__(self, id, name, *workers_list):
		assert isinstance(id, int), 'wrong id'
		assert isinstance(name, str), 'wrong departament name'

		self.id = id
		self.name = name
		if ()==workers_list: self.workers_list = [] #пришлось поставить костыль чтобы избежать static переменной
		else: self.workers_list = workers_list[0]

	def __repr__(self):
		return str(self.id)

	def __str__(self):
		return f'{self.name} departament: {self.workers_list}'

	def __getitem__(self, key):
		return self.workers_list[key]

	def add_worker(self, *args, **kwargs):
		self.workers_list.append(Worker(*args, **kwargs))

class Worker:
	def __init__(self, first_name, last_name, birthday, position, salary, kids=[]):
		assert isinstance(first_name, str), 'wrong firstname'
		assert isinstance(last_name, str), 'wrong lastname'
		assert isinstance(birthday, str), 'birthday must be string-like'
		assert isinstance(position, str), 'position must be string-like'
		assert isinstance(salary, int), 'salary must be a number'
		assert salary > 0

		birthday = list(map(int, birthday.split('.')))
		assert 1<=birthday[0]<=31
		assert 1<=birthday[1]<=12
		assert 1900<birthday[2]<=today_date[2]-18

		self.first_name = first_name.lower().capitalize()
		self.last_name = last_name.lower().capitalize()
		self.birthday = birthday
		self.position = position
		self.salary = salary
		self.kids = []

	def __repr__(self):
		return str(f'[{self.first_name} {self.last_name}, birthday: {self.birthday}, position: {self.position}, salary: {self.salary}]\n')

	def add_kid(self, *args, **kwargs):
		self.kids.append(Kid(*args, **kwargs))

class Kid:
	def __init__(self, first_name, last_name, birthday):
		assert isinstance(first_name, str), 'wrong firstname'
		assert isinstance(last_name, str), 'wrong lastname'
		assert isinstance(birthday, str), 'birthday must be in format XX.XX.XXXX'

		self.birthday = list(map(int, birthday.split('.')))

		self.firstname = first_name.lower().capitalize()
		self.lastname = last_name.lower().capitalize()
	
		if today_date[2]-self.birthday[2]<18:
			self.adult = False

		elif today_date[2]-self.birthday[2]==18:
			if today_date[1]-self.birthday[1]>0:
				self.adult = False

			elif today_date[1]-self.birthday[1]==0:
				if today_date[0]-self.birthday[0]>0:
					self.adult = False

			else:
				self.adult = True

		else:
			self.adult = True

	def __repr__(self):
		return f'{self.firstname} {self.lastname} {self.birthday}'


if __name__=='__main__':
	today_date = [28, 5, 2019]

	company = Company('GreatCompany', 'street 43', 234234)

	company.add_depart(0, 'dev')
	company.add_depart(1, 'advert')

	company[0].add_worker('Sam', 'Gets', '23.01.1988', 'backend', 20000)
	company[0].add_worker('Max', 'SDG', '05.05.1988', 'frontend', 14000)
	company[0].add_worker('Dmitry', 'dfgas', '12.06.1984', 'CEO', 100000)
	company[1].add_worker('Alex', 'sdfg', '04.05.1981', 'CEO', 100000)
	company[1].add_worker('Egor', 'adfg', '02.03.1985', 'manager', 1000)
	company[1].add_worker('Anton', 'sdfgds', '07.02.1983', 'hr', 5000)
	company[1].add_worker('Mikhail', 'sfdg', '02.05.1985', 'callmanager', 2500)

	company[0][1].add_kid('Lisa', 'Fsdf', '23.04.2005')
	company[1][2].add_kid('Max', 'SFhsd', '23.07.2006')
	company[1][2].add_kid('Alex', 'SFhgfshgf', '23.07.1995')
	company[1][2].add_kid('Eva', 'SFhgfshgf', '23.07.2008')

	#print(company) #полный список отделов предприятия
	#print(company[0]) #полный список кадров в отделе
	#print(company.get_ceo()) #руководители отделов
	#print(company.get_kids()) #список детей работников
	print(company.get_poor_workers()) #получить список работников с низкой зарплатой
