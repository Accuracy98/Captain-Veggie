# Author: Zhicheng Yang
# Date: 11/22/2023
# Description: Create a class named snake

from Creature import Creature
"""
A class representing a Snake in the game.

The Snake class is a subclass of Creature and inherits its properties and methods. 
It is initialized with a specific position on the game field and represented by the 
symbol 'S'.

Attributes:
- Inherits x and y coordinates from the Creature class.

Methods:
- __init__(self, x: int, y: int) -> None:
    Initializes a new Snake with the given x and y coordinates and the symbol 'S'.

Example:
    snake = Snake(5, 10)  # Creates a Snake object at position (5, 10) on the game field.
"""



class Snake(Creature):
    """
    Initializes a new Snake with the given x and y coordinates.

    Parameters:
    - x (int): The x-coordinate of the Snake's position on the game field.
    - y (int): The y-coordinate of the Snake's position on the game field.
    """
    def __init__(self, x: int, y: int) -> None:
        super().__init__("S", x, y)
