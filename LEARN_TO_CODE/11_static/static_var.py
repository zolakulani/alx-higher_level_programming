#!/usr/bin/python3

class dog:

    """This is varible"""
    num_of_dogs = 0

    def __init__(self, name="unknown"):
        self.name = name

        """You reference the variable by
        preceding with class naem"""
        dog.num_of_dogs += 1

    @staticmethod
    def getNumOfDogs():
        print("There is {} number of dogs".format(dog.num_of_dogs))

def main():
    spot = dog("spot")
    doug = dog("doug")
    spot.getNumOfDogs()

main()
