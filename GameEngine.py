import csv
import random

class GameEngine:
    def __init__(self) -> None:
        self.__NUMBEROFVEGGIES = 30
        self.__NUMBEROFRABBITS = 5
        self.__HIGHSCOREFILE = "highscore.data"
        self.__field = []
        self.__rabbits = []
        self.__caption = None
        self.__vegetables = []
        self.__score = 0

    def initVeggies(self):
        while True:
            file_name = input("Please enter the name of the vegetable point file: ")
            try:
                with open(file_name,"r") as file:
                    reader = csv.reader(file)
                    file_size = next(reader)
                    width, height = int(file_size[1]), int(file_size[2])
                    self.__field = [[None for _ in range(width)] for _ in range(height)]
            except FileNotFoundError:
                print(f"{file_name} does not exist!")

    def initCaption(self):
        ...

    def initRabbits(self):
        ...

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
    GameEngine()
