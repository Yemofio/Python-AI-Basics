class Person:
    def __init__(self, name, age):
        self.name = name   # Public attribute
        self.age = age     # Public attribute
        
    def say_hello(self):  # Public method
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
        
p = Person("Diggs", 20)
p.say_hello()  # Output: "Hello, my name is Giggs and I am 20 years old."
