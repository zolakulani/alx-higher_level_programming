#!/usr/bin/python3
class Dog:
 
    # This is a static variable
    num_of_dogs = 0
 
    def __init__(self, name="Unknown"):
        self.name = name
 
        # You reference the static variable by proceeding
        # it with the class name
        Dog.num_of_dogs += 1
 
    @staticmethod
    def getNumOfDogs():
        print("There are currently {} dogs".format(Dog.num_of_dogs))
 
def main():
 
    spot = Dog("Spot")
 
    doug = Dog("Doug")
 
    spot.getNumOfDogs()
 
 
main()
