from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Starting car engine.")

class Motorcycle(Vehicle):
    def start_engine(self):
        print("Starting motorcycle engine.")

v = Vehicle()   # Error: Can't instantiate abstract class Vehicle with abstract methods start_engine

c = Car()
m = Motorcycle()

c.start_engine()   # Output: Starting car engine.
m.start_engine()   # Output: Starting motorcycle engine.
