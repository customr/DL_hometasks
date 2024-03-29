import random


class Car:
	"""A car class

	Attributes:
		id (int): car identificator
		model (str): model of the car
		country (str): country of the car
		year (int): year of the car production
		engine_cap (float or int): engine capacity of the car
		price (float or int): price of the car
	"""
	def __init__(self, model, country, year, engine_cap, price):
		"""
		Args:
			model (str): model of the car
			country (str): country of the car
			year (int): year of the car production
			engine_cap (float or int): engine capacity of the car
			price (float or int): price of the car
		"""
		assert isinstance(model, str), 'Model must be a string-like'
		assert isinstance(country, str), 'Country must be a string-like'
		assert isinstance(year, int), 'Year must be a string-like'
		assert any([isinstance(engine_cap, float), isinstance(engine_cap, int)]), 'Engine capacity must be a float or int'
		assert any([isinstance(price, float), isinstance(price, int)]), 'Price must be a float or int'
		assert price > 0, 'Price must be a positive number'
		assert engine_cap > 0, 'Engine capacity must be a positive number'
		assert 1900 < year < 2019, 'Wrong year'

		self.id = random.randint(100000, 999999)
		self.model = model
		self.country = country.capitalize()
		self.year = year
		self.engine_cap = float(engine_cap)
		self.price = float(price)
		self.popularity = 0

	def __add__(self, dealer):
		"""Adds car to the dealership 

		Args:
			dealer (class CarDealership): dealer of cars
		
		Returns:
			dealership __radd__ method
		"""
		assert dealer.__class__.__name__=='CarDealership'
		return dealer.__radd__(self)

	def __radd__(self, dealer):
		"""Adds car to the dealership 

		Args:
			dealer (class CarDealership): dealer of cars
		
		Returns:
			dealership __add__ method
		"""
		assert dealer.__class__.__name__=='CarDealership'
		return dealer.__add__(self)

	def __repr__(self):
		"""
		Returns:
			str: car identifical number
		"""
		return str(self.id)

	def __str__(self):
		"""Print specification of the car and makes it more popular

		Returns:
			str: car specification
		"""
		self.popularity += 1
		return f'#{self.id}\nModel: {self.model}\nCountry: {self.country}\nYear: {self.year}\nEngine capacity: {self.engine_cap}\nPrice: {self.price} $\n'


class Lorry(Car):
	"""A lorry class

	Attributes:
		id (int): lorry identificator
		model (str): model of the lorry
		country (str): country of the lorry
		year (int): year of the car production
		engine_cap (float or int): engine capacity of the lorry
		price (float or int): price of the lorry
		max_weight (float or int): max weight for this lorry
	"""
	def __init__(self, model, country, year, engine_cap, price, max_weight):
		assert any([isinstance(max_weight, float), isinstance(max_weight, int)]), 'max_weight must be a float or int'

		super().__init__(model, country, year, engine_cap, price)
		self.max_weight = float(max_weight)

	def __str__(self):
		return super().__str__()+f'Max weight: {self.max_weight}\n' 


class CarDealership:
	"""Dealer of cars
	
	Arrtibutes:
		name (str): name of the dealership
		address(str): address of the dealership
		cars (list): list of the cars. Defaults to empty list
		lorrys (list): list of the lorrys. Defaults to empty list

	"""
	def __init__(self, name, address, cars=[], lorrys=[]):
		assert isinstance(name, str)
		assert isinstance(address, str)
		assert isinstance(cars, list)
		assert isinstance(lorrys, list)
		
		self.name = name
		self.address = address
		self.cars = cars
		self.lorrys = lorrys

	def __getitem__(self, id):
		"""Returns item by its identifier
		
		Args:
			id (int): item identifier

		Returns:
			The car or the lorry

		"""
		for car in list(self.cars+self.lorrys):
			if car.id == id:
				return car

	def __add__(self, cls):
		"""Adds the car or the lorry to the dealership

		Args:
			cls (class): Car or Lorry

		Raises:
			TypeError: if cls is not the Car or the Lorry
		"""
		type = cls.__class__.__name__

		if type == 'Car':
			print('*'*50)
			print(f'+++ADDED NEW CAR TO THE DEALERSHIP')
			print('*'*50)
			print(cls)
			self.cars.append(cls)

		elif type == 'Lorry':
			print('*'*50)
			print(f'+++ADDED NEW LORRY TO THE DEALERSHIP')
			print('*'*50)
			print(cls)
			self.lorrys.append(cls)

		else:
			raise TypeError('Unknown type')

	def __radd__(self, cls):
		"""
		The same as __add__ but on the other side
		"""
		return self.__add__(cls)

	def __sub__(self, id):
		"""Removes the car or the lorry from the dealership by its identifier
		
		Args:
			id (int): identifier
		"""
		assert isinstance(id, int)

		print('*'*50)
		print(f'---ITEM #{id} HAVE BEEN REMOVED FROM THE DEALERSHIP')
		print('*'*50)

		for n, car in enumerate(self.cars):
			if id == car.id:
				del(self.cars[n])

		for n, lorry in enumerate(self.lorrys):
			if id == lorry.id:
				del(self.lorrys[n])

	def __repr__(self):
		"""Describes dealership"""
		return f'{self.name}, {self.address}\n'

	def __str__(self):
		"""Outputs all items of dealership"""
		s = self.__repr__()

		for item in list(self.cars+self.lorrys):
			s = s + item.__str__() + '\n'

		return s

	def get_popular_item(self):
		"""Get the most popular item in the dealership by its popularity critery

		Returns:
			the Car or the Lorry
			
		"""
		m = 0
		for item in list(self.cars+self.lorrys):
			if item.popularity > m:
				m = item.popularity
				pop = item

		if m==0:
			return 'NO POPULAR ITEMS'
		else:
			return pop

if __name__=='__main__':
	dealer = CarDealership('DealerShip', 'Fall street, 54')
	car1 = Car('Nissan 234', 'Japan', 2005, 205, 10000)
	car2 = Car('Mazda RX7', 'Japan', 2007, 300, 15000)
	lor1 = Lorry('Mercedes GlS', 'Germany', 2009, 500, 25000, 600)

	dealer + car1 #добавляет car1 к дилеру в базу
	dealer + car2
	dealer + lor1

	#print(dealer)

	#dealer - car2.id #удаляет car2 из базы

	#print(dealer)

	# print(car1) #просматриваем машину, повышая ее популярность
	# print('###MOST POPULAR CAR:')
	# print(dealer.get_popular_item())

	# while True: #для мгновенных тестов
	# 	eval(input())