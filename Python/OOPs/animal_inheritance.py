class Animal:
    def __init__(self,colour):
        self.c = colour 
    def introduce(self):
        print("Hello I am an animal")
    def makeSound(self):
        print("Making sound")

class Dog(Animal):
    def child(self):
        print("Puppy")
    def makeSound(self):
        print("Bow")
    

wild_animal = Animal("Brown")
p = Dog("white")
p.introduce()
wild_animal.makeSound()

class Cat(Animal):
    def makeSound(self):
        print("Meow")

kitten = Cat("caramel")
#function overriding 
kitten.makeSound()
p.makeSound()