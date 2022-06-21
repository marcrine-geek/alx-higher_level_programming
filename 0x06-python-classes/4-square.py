#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Defines a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the square."""
        return(self.__size)

    @size.setter
    def size(self, value):
        """A property setter."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Current square area."""
        return(self.__size * self.__size)
