import csv
import random
from Captain import Captain
from Creature import Creature
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
        self.__captain: Captain | None = None
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

    def initCaptain(self):
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
                    rabbit = Rabbit(x, y)
                    self.__rabbits.append(rabbit)
                    self.__field[x][y] = rabbit
                    break

    def initializeGame(self):
        self.initVeggies()
        self.initCaptain()
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
        height = len(self.__field)
        width = len(self.__field[0])
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, 1),
            (0, -1),
            (0, 0),
            (1, 1),
            (1, 0),
            (1, -1),
        ]
        for rabbit in self.__rabbits:
            x = rabbit.getX()
            y = rabbit.getY()
            dx, dy = random.choice(directions)
            new_x, new_y = x + dx, y + dy

            if 0 <= new_x < width and 0 <= new_y < height:
                if self.__field[new_x][new_y] is None or isinstance(
                    self.__field[new_x][new_y], Veggie
                ):
                    self.__field[x][y] = None
                    rabbit.setX(new_x)
                    rabbit.setY(new_y)
                    self.__field[new_x][new_y] = rabbit

    def moveCptVertical(self, movement):
        height = len(self.__field)
        if self.__captain is None:
            return
        new_y = self.__captain.getY() + movement
        if 0 <= new_y < height:
            new_position = self.__field[self.__captain.getX()][new_y]
            if isinstance(new_position, Veggie):
                print(f"A delicious {new_position.getName()} has been found")
                self.__captain.addVeggie(new_position)
                self.__score += 1
                self.__field[self.__captain.getX()][self.__captain.getY()] = None
                self.__captain.setY(new_y)
                self.__field[self.__captain.getX()][new_y] = self.__captain
            elif isinstance(new_position, Rabbit):
                return
            elif new_position is None:
                self.__field[self.__captain.getX()][self.__captain.getY()] = None
                self.__captain.setY(new_y)
                self.__field[self.__captain.getX()][new_y] = self.__captain

    def moveCptHorizontal(self, movement):
        width = len(self.__field[0])
        if self.__captain is None:
            return
        new_x = self.__captain.getX() + movement
        if 0 <= new_x < width:
            new_position = self.__field[new_x][self.__captain.getY()]
            if isinstance(new_position, Veggie):
                print(f"A delicious {new_position.getName()} has been found")
                self.__captain.addVeggie(new_position)
                self.__score += 1
                self.__field[self.__captain.getX()][self.__captain.getY()] = None
                self.__captain.setX(new_x)
                self.__field[new_x][self.__captain.getY()] = self.__captain
            elif isinstance(new_position, Rabbit):
                return
            elif new_position is None:
                self.__field[self.__captain.getX()][self.__captain.getY()] = None
                self.__captain.setX(new_x)
                self.__field[new_x][self.__captain.getY()] = self.__captain

    def moveCaptain(self):
        if self.__captain is None:
            return
        directions = input(
            "Would you like to move up(W), down(S), left(A), or right(D):"
        ).lower()
        if directions == "w":
            if self.__captain.getY() > 0:
                self.moveCptVertical(-1)
            else:
                print("Can not move")
        elif directions == "s":
            if self.__captain.getY() < len(self.__field) - 1:
                self.moveCptVertical(1)
            else:
                print("Can not move")
        elif directions == "a":
            if self.__captain.getX() > 0:
                self.moveCptHorizontal(-1)
            else:
                print("Can not move")
        elif directions == "d":
            if self.__captain.getX() < len(self.__field[0]) - 1:
                self.moveCptHorizontal(1)
            else:
                print("Can not move")
        else:
            print(f"{directions} is not a valid option")

    def gameOver(self):
        ...

    def highScore(self):
        ...


if __name__ == "__main__":
    game_engine = GameEngine()
    game_engine.initVeggies()
    game_engine.initCaptain()
    game_engine.initRabbits()
    game_engine.moveCaptain()
    game_engine.moveRabbits()
    game_engine.moveCptVertical(1)
    game_engine.moveCptHorizontal(1)
    game_engine.moveCaptain()
