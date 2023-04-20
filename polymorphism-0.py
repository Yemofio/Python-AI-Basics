class Animal:
    def make_sound(self):
        pass
        
class Dog(Animal):
    def make_sound(self):
        print("Woof!")
        
class Cat(Animal):
    def make_sound(self):
        print("Meow!")
        
def animal_sounds(animal):
    animal.make_sound()
    
dog = Dog()
cat = Cat()

animal_sounds(dog)  # Output: "Woof!"
animal_sounds(cat)  # Output: "Meow!"
