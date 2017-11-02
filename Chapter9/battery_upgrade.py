"""
Exercise 9-9
Use the electric_car.py program.

Add a method to Battery called upgrade_battery()
which should check the size and if it isn't 85
set it to 85

Make an electric car with a default batter size,
call get_range(), call upgrade_battery(), then
call get_range() again
"""

class Car():
	"""A simple representation of a car."""

	def __init__(self, make, model, year):
		"""Initialze attributes to describe a car."""

		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		"""Display the car's mileage"""
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_odometer(self, mileage):
		"""
		Set the odometer reading to the given value
		Reject the change if they try to lower the mileage
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		"""Add the given amount of miles to the odometer reading"""
		self.odometer_reading += miles

	def fill_gas_tank(self):
		"""Fill gas tank to full in a car"""
		print("Gas tank is now full")


class Battery():
	"""A simple representation of a battery for an electric car."""

	def __init__(self, battery_size=70):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print a statement describing the batter size."""
		print("This car has a " + str(self.battery_size) + "-kwh battery.")

	def get_range(self):
		"""Print the range the battery provides"""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270

		message = "This car can go approximately " + str(range)
		message += " miles on a full charge"
		print(message)

	def upgrade_battery(self):
		"""Set the batter size to 85 if it isn't already"""
		if self.battery_size != 85:
			self.battery_size = 85


class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles"""

	def __init__(self, make, model, year):
		"""
		Initialize attributes of the parent class
		Then initialize attributes specific to electric cars
		"""
		super().__init__(make,model,year)
		self.battery = Battery()


	def fill_gas_tank(self):
		"""Electric cars don't have gas tanks"""
		print("This car doesn't need a gas tank!")


electric_car = ElectricCar('audi','tesla s', '2016')
electric_car.battery.get_range()
electric_car.battery.upgrade_battery()
electric_car.battery.get_range()