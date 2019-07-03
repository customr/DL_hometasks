import random
import json


class Car:
	def __init__(self, model, country, year, engine_cap, price):
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
		assert dealer.__class__.__name__=='CarDealership'
		return dealer.__radd__(self)

	def __radd__(self, dealer):
		assert dealer.__class__.__name__=='CarDealership'
		return dealer.__add__(self)

	def __repr__(self):
		return str(self.id)

	def __str__(self):
		self.popularity += 1
		return f'#{self.id}\nModel: {self.model}\nCountry: {self.country}\nYear: {self.year}\nEngine capacity: {self.engine_cap}\nPrice: {self.price} $\n'


class Lorry(Car):
	def __init__(self, model, country, year, engine_cap, price, max_weight):
		assert any([isinstance(max_weight, float), isinstance(max_weight, int)]), 'max_weight must be a float or int'

		super().__init__(model, country, year, engine_cap, price)
		self.max_weight = float(max_weight)

	def __str__(self):
		return super().__str__()+f'Max weight: {self.max_weight}\n' 


class CarDealership:
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
		for car in list(self.cars+self.lorrys):
			if car.id == id:
				return car

	def __add__(self, cls):
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
		return self.__add__(cls)

	def __sub__(self, id):
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
		return f'{self.name}, {self.address}\n'

	def __str__(self):
		s = self.__repr__()

		for item in list(self.cars+self.lorrys):
			s = s + item.__str__() + '\n'

		return s

	def get_popular_item(self):
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

	dealer + car1
	dealer + car2
	dealer + lor1

	#print(dealer)

	dealer - car2.id

	#print(dealer)

	# print(car1) #просматриваем машину, повышая ее популярность
	# print('###MOST POPULAR CAR')
	# print(dealer.get_popular_item())