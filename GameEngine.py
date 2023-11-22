import csv
import random
import pickle
import pathlib
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
        self.__captain: Captain | None = None
        self.__vegetables: list[Veggie] = []
        self.__score = 0

    def initVeggies(self) -> None:
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

    def initCaptain(self) -> None:
        height = len(self.__field)
        width = len(self.__field[0])
        while True:
            x, y = random.randint(0, width - 1), random.randint(0, height - 1)
            if self.__field[x][y] is None:
                self.__captain = Captain(x, y)
                self.__field[x][y] = self.__captain
                break

    def initRabbits(self) -> None:
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

    def initializeGame(self) -> None:
        self.initVeggies()
        self.initCaptain()
        self.initRabbits()

    def remainingVeggies(self) -> int:
        counter = 0
        for row in self.__field:
            for entity in row:
                if isinstance(entity, Veggie):
                    counter += 1
        return counter

    def intro(self) -> None:
        print("Welcome to Captain Veggie!")
        print("The rabbits have invaded your garden and you must harvest")
        print("as many vegetables as possible before the rabbits eat them")
        print("all! Each vegetable is worth a different number of points")
        print("so go for the high score!")
        print()
        print("The vegetables are:")
        for v in self.__vegetables:
            print(v)
        print()
        print("Captain Veggie is V, and the rabbits are R's.")
        print()
        print("Good luck!")

    def printField(self) -> None:
        print(self.__captain.getX())
        print(self.__captain.getY())
        width = len(self.__field[0]) * 3 + 2
        print("#" * width)
        for row in self.__field:
            print("#", end="")
            for entity in row:
                if entity is None:
                    print("   ", end="")
                else:
                    print(f" {entity.getSymbol()} ", end="")
            print("#")
        print("#" * width)

    def getScore(self) -> int:
        return self.__score

    def moveRabbits(self) -> None:
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

    def __updateCptLocation(self, new_x: int, new_y: int) -> None:
        if self.__captain is None:
            return
        self.__field[self.__captain.getX()][self.__captain.getY()] = None
        self.__captain.setX(new_x)
        self.__captain.setY(new_y)
        self.__field[new_x][new_y] = self.__captain

    def __moveCpt(self, movement_x: int = 0, movement_y: int = 0) -> None:
        if self.__captain is None:
            return
        height = len(self.__field)
        width = len(self.__field[0])
        new_x = self.__captain.getX() + movement_x
        new_y = self.__captain.getY() + movement_y
        if 0 <= new_x < height and 0 <= new_y < width:
            entity = self.__field[new_x][new_y]
            if isinstance(entity, Veggie):
                print(f"Yummy! A delicious {entity.getName()}")
                self.__captain.addVeggie(entity)
                self.__score += entity.getPoints()
                self.__updateCptLocation(new_x, new_y)
            elif isinstance(entity, Rabbit):
                print("Don't step on the bunnies!")
                return
            elif entity is None:
                self.__updateCptLocation(new_x, new_y)
        else:
            print("You can't move that way!")

    def moveCptVertical(self, movement: int) -> None:
        self.__moveCpt(movement_x=movement)

    def moveCptHorizontal(self, movement: int) -> None:
        self.__moveCpt(movement_y=movement)

    def moveCaptain(self) -> None:
        if self.__captain is None:
            return
        directions = input(
            "Would you like to move up(W), down(S), left(A), or right(D):"
        ).lower()
        if directions == "w":
            self.moveCptVertical(-1)
        elif directions == "s":
            self.moveCptVertical(1)
        elif directions == "a":
            self.moveCptHorizontal(-1)
        elif directions == "d":
            self.moveCptHorizontal(1)
        else:
            print(f"{directions} is not a valid option")

    def gameOver(self) -> None:
        if self.__captain is None:
            return
        print("GAME OVER!")
        print("You managed to harvest the following vegetables:")
        for v in self.__captain.getVeggies():
            print(v.getName())
        print(f"Your score was: {self.__score}")

    def highScore(self) -> None:
        history_scores: list[tuple[str, int]] = list()
        if pathlib.Path(self.__HIGHSCOREFILE).exists():
            with open(self.__HIGHSCOREFILE, "rb") as f:
                history_scores = pickle.load(f)
        name = input("Please enter your three initials to go on the scoreboard: ")
        i = 0
        for i in range(len(history_scores)):
            if self.__score > history_scores[i][1]:
                break
        history_scores.insert(i, (name, self.__score))

        print()
        print("HIGH SCORES")
        print("Name    Score")
        for e in history_scores:
            print(f"{e[0]}     {e[1]}")

        with open(self.__HIGHSCOREFILE, "w+b") as f:
            pickle.dump(history_scores, f)
