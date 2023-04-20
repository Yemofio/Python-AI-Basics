class Car:
    def __init__(self, make, model, year):
        self.make = make    # Public attribute
        self.model = model  # Public attribute
        self.year = year    # Public attribute
        self.__mileage = 0  # Private attribute
        
    def get_description(self):
        return f"{self.year} {self.make} {self.model}"
        
    def get_mileage(self):
        return self.__mileage
        
    def add_mileage(self, miles):
        self.__mileage += miles

        
my_car = Car("Honda", "Civic", 2020)
print(my_car.get_description())  # Output: "2020 Honda Civic"

print(my_car.get_mileage())      # Output: 0
my_car.add_mileage(100)
print(my_car.get_mileage())      # Output: 100
