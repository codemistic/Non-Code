class Car:
    def __init__(self,mileage,colour):
        self.m = mileage 
        self.c = colour 
    def getMileage(self):
        return self.m 
    def getColour(self):
        return self.m 
    def greet(self):
        print("Hello I am a car ")

model1 = Car(55,"red")
model2 = Car(56,"Blue")

print(model1.getMileage)()
model2.greet()

model3 = Car(23,"Green")
