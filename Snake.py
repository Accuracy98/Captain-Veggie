# Author: Zhicheng Yang
# Date: 11/22/2023
# Description: Create a class named snake

from Creature import Creature


class Snake(Creature):
    def __init__(self, x: int, y: int) -> None:
        super().__init__("S", x, y)
