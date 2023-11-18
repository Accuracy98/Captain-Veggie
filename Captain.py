# Author: Zhekang Xu
# Date: 2023-11-18
# Description: Captain definition
from Creature import Creature
from Veggie import Veggie


class Captain(Creature):
    """
    A class representing a Captain creature.

    Attributes:
    - x (int): The x-coordinate of the Captain's position.
    - y (int): The y-coordinate of the Captain's position.
    - __veggies (list[Veggie]): A private list to store Veggie objects associated with the Captain.

    Methods:
    - __init__(self, x: int, y: int) -> None:
        Initializes a new Captain with the given x and y coordinates.

    - addVeggie(self, veggie: Veggie) -> None:
        Adds a Veggie object to the Captain's list of veggies.

    - getVeggies(self) -> list[Veggie]:
        Returns the list of Veggie objects associated with the Captain.

    - setVeggies(self, veggies: list[Veggie]) -> None:
        Sets the list of Veggie objects associated with the Captain.

    Note:
    The Captain class is a subclass of Creature and inherits its attributes and methods.
    """

    def __init__(self, x: int, y: int) -> None:
        self.__veggies: list[Veggie] = []
        super().__init__("V", x, y)

    def addVeggie(self, veggie: Veggie) -> None:
        """Adds a Veggie object to the Captain's list of veggies."""
        self.__veggies.append(veggie)

    def getVeggies(self) -> list[Veggie]:
        """Returns the list of Veggie objects associated with the Captain."""
        return self.__veggies

    def setVeggies(self, veggies: list[Veggie]) -> None:
        """Sets the list of Veggie objects associated with the Captain."""
        self.__veggies = veggies
