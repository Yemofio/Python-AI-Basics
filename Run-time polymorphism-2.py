#Runtime polymorphism can be achieved by defining a method with the same name in the subclass as in the parent class. 
#The subclass method must have the same method signature (i.e., the same name and parameters) as the parent class method 
#it is overriding. When an object of the subclass is created and the overridden method is called, the subclass method is 
#executed instead of the parent class method.

class Animal:
    def make_sound(self):
        print("Animal is making a sound.")

class Dog(Animal):
    def make_sound(self):
        print("Dog is barking.")

class Cat(Animal):
    def make_sound(self):
        print("Cat is meowing.")

a = Animal()
d = Dog()
c = Cat()

a.make_sound()   # Output: Animal is making a sound.
d.make_sound()   # Output: Dog is barking.
c.make_sound()   # Output: Cat is meowing.




#the Shape class defines an abstract area method that is meant to be overridden by its subclasses. The Rectangle and Circle 
#classes both inherit from the Shape class and provide their own implementations of the area method that are specific to their
#shapes. When the area method is called on an object of each class, the appropriate subclass method is executed.
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

r = Rectangle(5, 10)
c = Circle(3)

print(r.area())   # Output: 50
print(c.area())   # Output: 28.26



