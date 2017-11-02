import car_module

my_beetle = car_module.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
print("\n")

my_tesla = car_module.ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())