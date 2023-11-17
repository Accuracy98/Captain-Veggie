# Author: Zhicheng Yang
# Date: 11/17/2023
# Description: Creature definition

from FieldInhabitant import FieldInhabitant


class Creature(FieldInhabitant):
    """
    A class representing a creature in a field.

    Attributes:
    - symbol (str): The symbol representing the creature.
    - x (int): The x-coordinate of the creature's position.
    - y (int): The y-coordinate of the creature's position.

    Methods:
    - getX(): Get the x-coordinate of the creature's position.
    - setX(x: int): Set the x-coordinate of the creature's position.
    - getY(): Get the y-coordinate of the creature's position.
    - setY(y: int): Set the y-coordinate of the creature's position.

    Inherits from the FieldInhabitant class.
    """

    def __init__(self, symbol: str, x: int, y: int) -> None:
        self.__x = x
        self.__y = y
        super().__init__(symbol)

    def getX(self) -> int:
        """
        Get the x-coordinate of the creature's position.

        Returns:
        - int: The x-coordinate of the creature's position.
        """
        return self.__x

    def setX(self, x: int) -> None:
        """
        Set the x-coordinate of the creature's position.

        Parameters:
        - x (int): The new x-coordinate for the creature's position.

        Returns:
        - None
        """
        self.__x = x

    def getY(self) -> int:
        """
        Get the y-coordinate of the creature's position.

        Returns:
        - int: The y-coordinate of the creature's position.
        """
        return self.__y

    def setY(self, y: int) -> None:
        """
        Set the y-coordinate of the creature's position.

        Parameters:
        - y (int): The new y-coordinate for the creature's position.

        Returns:
        - None
        """
        self.__y = y
