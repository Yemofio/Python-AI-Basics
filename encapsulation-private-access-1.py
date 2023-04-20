class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute
        
    def __say_hello(self): # Private method
        print(f"Hello, my name is {self.__name} and I am {self.__age} years old.")
        
    def greet(self):
        self.__say_hello()
        
p = Person("Diggs", 20)
p.greet()  # Output: "Hello, my name is Diggs and I am 20 years old."
