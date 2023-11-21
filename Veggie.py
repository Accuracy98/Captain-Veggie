# Author: Zhicheng Yang
# Date: 11/17/2023
# Description: Veggie definition

from FieldInhabitant import FieldInhabitant


class Veggie(FieldInhabitant):
    """
    A class representing a vegetable in a field.

    Attributes:
    - symbol (str): The symbol representing the vegetable.
    - name (str): The name of the vegetable.
    - points (int): The points associated with the vegetable.

    Methods:
    - getName(): Get the name of the vegetable.
    - setName(name: str): Set the name of the vegetable.
    - getPoints(): Get the points associated with the vegetable.
    - setPoints(points: int): Set the points associated with the vegetable.
    - __str__(): Return a string representation of the vegetable.

    Inherits from the FieldInhabitant class.
    """

    def __init__(self, symbol: str, name: str, points: int) -> None:
        self.__name = name
        self.__points = points
        super().__init__(symbol)

    def getName(self) -> str:
        """
        Get the name of the vegetable.

        Returns:
        - str: The name of the vegetable.
        """
        return self.__name

    def setName(self, name: str) -> None:
        """
        Set the name of the vegetable.

        Parameters:
            - name (str): The new name for the vegetable.

        Returns:
            - None
        """
        self.__name = name

    def getPoints(self) -> int:
        """
        Get the points associated with the vegetable.

        Returns:
        - int: The points associated with the vegetable.
        """
        return self.__points

    def setPoints(self, points: int) -> None:
        """
        Set the points associated with the vegetable.

        Parameters:
        - points (int): The new points value for the vegetable.

        Returns:
        - None
        """
        self.__points = points

    def __str__(self) -> str:
        return f"{self._symbol}: {self.__name} {self.__points} points"
