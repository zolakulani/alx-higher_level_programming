#!/usr/bin/python3
"""
Defines a base model class.
"""
class Base:
    """
    Represents the base model
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """
        Initializes a Base object.

        Args:
            id (int, optional): The ID of the object. If None, a new ID is generated
            automatically. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
