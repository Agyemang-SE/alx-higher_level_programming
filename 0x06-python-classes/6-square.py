#!/usr/bin/python3

"""Class Square"""

class Square():
    """Private instance attribute: size:

        property def size(self): to retrieve it
        property setter def size(self, value): to set it:
            size must be an integer, otherwise raise a TypeError 
            exception with the message size must be an integer
            if size is less than 0, raise a ValueError exception 
            with the message size must be >= 0

    Private instance attribute: position:
        property def position(self): to retrieve it
        property setter def position(self, value): to set it:
            position must be a tuple of 2 positive integers, 
            otherwise raise a TypeError exception with the message 
            position must be a tuple of 2 positive integers
    Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):
    Public instance method: def area(self): that returns the current square area
    Public instance method: def my_print(self): that prints in stdout the square with the character #:
        if size is equal to 0, print an empty line
        position should be use by using space - Don’t fill lines 
        by spaces when position[1] > 0
    """

    def __init__(self, size=0, position=(0, 0)):
        """ Method - Initialize.
        Args:
            self (class): This class
            size (int): Size of the square
        """
        self.size = size
        self.position = position

    def area(self):
        """ Method - Returns the current square area.
        Args:
            self (class): This class
        """
        return (self.__size ** 2)

    def my_print(self):
        """ Method - prints in stdout the square with the character #.
        Args:
            self (class): This class
        """
        if self.__size:
            for i in range(self.position[1]):
                print()
            for j in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
        else:
            print()

    @property
    def size(self):
        """ Get - instance attribute size
        """
        return (self.__size)

    @property
    def position(self):
        """ Get - instance attribute position
        """
        return (self.__position)

    @size.setter
    def size(self, value):
        """ Set - instance attribute size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """ Set - instance attribute position
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(val, int) for val in value) or
                not all(val >= 0 for val in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
