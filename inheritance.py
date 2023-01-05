"""
Author: Aldiana Kucevic
Date: 30-12-2022
Function: Inheritance
"""

# voorbeeld met een car class



class Automobile:
    # __init__ methode accepteert arguments
    # make, model, mileage, and price

    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price

    def setMake(self, make):
        self.__make = make

    def setModel(self, model):
        self.__model = model

    def setMileage(self, mileage):
        self.__mileage = mileage

    def setPrice(self, price):
        self.__price = price

    def getMake(self):
        return self.__make

    def getModel(self):
        return self.__model

    def getMileage(self):
        return self.__mileage

    def getPrice(self):
        return self.__price

# alles hierboven is van de superclass Automobile, nu kunnen we specifieker werken

class Car(Automobile):

    # __init__ neemt weer dezelfde argumenten met een extra argument

    def __init__(self, make, model, mileage, price, doors):
        Automobile.__init__(self, make, model, mileage, price)

        self.__doors = doors

    def setDoors(self, doors):
        self.__doors = doors

    def getDoors(self):
        return self.__doors


import vechicles

def main():
    used_car = vechicles.Car("Audi", 2007, 12500, 21500.0, 4)
    print("Make: ", used_car.getMake())
    print("Model: ", used_car.getModel())
    print("Mileage: ", used_car.getMileage())
    print("Price: ", used_car.getPrice())
    print("Doors: ", used_car.getDoors())

main()

# hoe de layout er ongeveer uitziet