# Author: Zhekang Xu
# Date: 2023-11-18
# Description: Rabbit definition
from Creature import Creature


class Rabbit(Creature):
    """
    A class representing a Rabbit creature.

    Attributes:
    - x (int): The x-coordinate of the Rabbit's position.
    - y (int): The y-coordinate of the Rabbit's position.

    Methods:
    - __init__(self, x: int, y: int) -> None:
        Initializes a new Rabbit with the given x and y coordinates.

    Note:
    The Rabbit class is a subclass of Creature and inherits its attributes and methods.
    """

    def __init__(self, x: int, y: int) -> None:
        super().__init__("R", x, y)
