from FieldInhabitant import FieldInhabitant


class Veggie(FieldInhabitant):
    """A class representing a vegetable in a field.

    Attributes:
        symbol (str): The symbol representing the vegetable.
        name (str): The name of the vegetable.
        points (int): The points associated with the vegetable.

    Methods:
        getName(): Get the name of the vegetable.
        setName(name: str): Set the name of the vegetable.
        getPoints(): Get the points associated with the vegetable.
        setPoints(points: int): Set the points associated with the vegetable.
        __str__(): Get a string representation of the vegetable.

    """
    def __init__(self, symbol: str, name: str, points: int) -> None:
        self.__name = name
        self.__points = points
        super().__init__(symbol)

    def getName(self) -> str:
        return self.__name

    def setName(self, name: str) -> None:
        self.__name = name

    def getPoints(self) -> int:
        return self.__points

    def setPoints(self, points: int) -> None:
        self.__points = points

    def __str__(self) -> str:
        return f"{self.__name} {self.__points} points"
