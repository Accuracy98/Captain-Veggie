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
        ...

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
