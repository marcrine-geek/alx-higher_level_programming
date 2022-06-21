#!/usr/bin/python3

class Square:
    """A class that defines a square."""
    def __init__(self, size=0):
        """Instatiation."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """Returns current square area"""
        return(self.__size * self.__size)
