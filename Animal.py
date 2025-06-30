# Parent class (Base class)
class Animal:
    def _init_(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

# Child class (Derived class)
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

# Another Child class
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

# Create objects
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call methods
dog.speak()   # Output: Buddy says Woof!
cat.speak()   # Output: Whiskers says Meow!
