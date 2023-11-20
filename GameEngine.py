
import csv
import random
from Captain import Captain
from Veggie import Veggie
from FieldInhabitant import FieldInhabitant
from Rabbit import Rabbit


class GameEngine:
    def __init__(self) -> None:
        self.__NUMBEROFVEGGIES = 30
        self.__NUMBEROFRABBITS = 5
        self.__HIGHSCOREFILE = "highscore.data"
        self.__field: list[list[FieldInhabitant | None]] = []
        self.__rabbits: list[Rabbit] = []
        self.__caption: Captain | None = None
        self.__vegetables: list[Veggie] = []
        self.__score = 0

    def initVeggies(self):
        while True:
            file_name = input("Please enter the name of the vegetable point file: ")
            try:
                with open(file_name, "r") as file:
                    reader = csv.reader(file)
                    file_size = next(reader)
                    width, height = int(file_size[1]), int(file_size[2])
                    self.__field = [[None for _ in range(width)] for _ in range(height)]
                    for line in reader:
                        self.__vegetables.append(Veggie(line[1], line[0], int(line[2])))
                    for _ in range(self.__NUMBEROFVEGGIES):
                        while True:
                            x = random.randint(0, width - 1)
                            y = random.randint(0, height - 1)
                            if self.__field[x][y] is None:
                                self.__field[x][y] = random.choice(self.__vegetables)
                                break
                    break
            except FileNotFoundError:
                print(f"{file_name} does not exist!")

    def initCaption(self):
        height = len(self.__field)
        width = len(self.__field[0])
        while True:
            x, y = random.randint(0, width - 1), random.randint(0, height - 1)
            if self.__field[x][y] is None:
                self.__captain = Captain(x, y)
                self.__field[x][y] = self.__captain
                break

    def initRabbits(self):
        height = len(self.__field)
        width = len(self.__field[0])
        for _ in range(self.__NUMBEROFRABBITS):
            while True:
                x, y = random.randint(0, width - 1), random.randint(0, height - 1)
                if self.__field[x][y] is None:
                    rabbit = Rabbit(x,y)
                    self.__rabbits.append(rabbit)
                    self.__field[x][y] = rabbit
                    break

    def initializeGame(self):
        self.initVeggies()
        self.initCaption()
        self.initRabbits()

    def remainingVeggies(self):
        ...

    def intro(self):
        ...

    def printField(self):
        ...

    def getScore(self):
        ...

    def moveRabbits(self):
        ...

    def moveCptVertical(self, movement):
        ...

    def moveCptHorizontal(self, movement):
        ...

    def moveCaptain(self):
        ...

    def gameOver(self):
        ...

    def highScore(self):
        ...


if __name__ == "__main__":
    game_engine = GameEngine()
    game_engine.initVeggies()
    game_engine.initCaption()
    game_engine.initRabbits()
