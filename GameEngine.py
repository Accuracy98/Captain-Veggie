# Author: ZhiCheng Yang, Zhekang Xu
# Date: 2023-11-22
# Description: Represents the game engine for a fictional game called "Captain Veggie."

import csv
import random
import pickle
import pathlib
from Captain import Captain
from Veggie import Veggie
from FieldInhabitant import FieldInhabitant
from Rabbit import Rabbit
from Snake import Snake
from Creature import Creature


class GameEngine:
    """
    A class representing the game engine for Captain Veggie.

    Attributes:
    - __NUMBEROFVEGGIES (int): The number of vegetables in the game.
    - __NUMBEROFRABBITS (int): The number of rabbits in the game.
    - __HIGHSCOREFILE (str): The file name for storing high scores.
    - __field (list[list[FieldInhabitant | None]]): A 2D list representing the game field.
    - __rabbits (list[Rabbit]): A list of Rabbit objects in the game.
    - __captain (Captain | None): The Captain object in the game.
    - __vegetables (list[Veggie]): A list of Veggie objects in the game.
    - __score (int): The current score of the game.

    Methods:
    - __init__(self) -> None:
        Initializes a new GameEngine object.

    - initVeggies(self) -> None:
        Initializes the vegetables in the game.

    - initCaptain(self) -> None:
        Initializes the Captain in the game.

    - initRabbits(self) -> None:
        Initializes the rabbits in the game.

    - initializeGame(self) -> None:
        Initializes the entire game.

    - remainingVeggies(self) -> int:
        Returns the number of remaining vegetables in the game.

    - intro(self) -> None:
        Prints the game introduction.

    - printField(self) -> None:
        Prints the current state of the game field.

    - getScore(self) -> int:
        Returns the current score of the game.

    - moveRabbits(self) -> None:
        Moves the rabbits randomly on the game field.

    - moveCptVertical(self, movement: int) -> None:
        Moves the Captain vertically.

    - moveCptHorizontal(self, movement: int) -> None:
        Moves the Captain horizontally.

    - moveCaptain(self) -> None:
        Accepts user input to move the Captain.

    - gameOver(self) -> None:
        Prints the game over message with the final score.

    - highScore(self) -> None:
        Displays and updates the high scores.
    """

    def __init__(self) -> None:
        self.__NUMBEROFVEGGIES = 30
        self.__NUMBEROFRABBITS = 5
        self.__HIGHSCOREFILE = "highscore.data"
        self.__field: list[list[FieldInhabitant | None]] = []
        self.__rabbits: list[Rabbit] = []
        self.__captain: Captain | None = None
        self.__vegetables: list[Veggie] = []
        self.__score = 0
        self.__snake = None

    def initSnake(self):
        height = len(self.__field)
        width = len(self.__field[0])
        while True:
            x, y = random.randint(0, height - 1), random.randint(0, width - 1)
            if self.__field[x][y] is None:
                self.__snake = Snake(x, y)
                self.__field[x][y] = self.__snake
                break

    def initVeggies(self) -> None:
        """
        Initializes the vegetables in the game.

        The method prompts the user to enter the name of the vegetable point file, reads the
        file to get the dimensions of the game field, populates the game field with vegetables,
        and randomly places the specified number of vegetables on the field.

        Raises:
        - FileNotFoundError: If the specified file does not exist.

        Note:
        This method assumes that the vegetable point file is a CSV file with the following format:
        - The first line contains the width and height of the game field.
        - Each subsequent line contains the name, symbol, and points of a vegetable.
        """
        while True:
            file_name = input("Please enter the name of the vegetable point file: ")
            try:
                with open(file_name, "r") as file:
                    reader = csv.reader(file)
                    file_size = next(reader)
                    height, width = int(file_size[1]), int(file_size[2])
                    self.__field = [[None for _ in range(width)] for _ in range(height)]
                    for line in reader:
                        self.__vegetables.append(Veggie(line[1], line[0], int(line[2])))
                    for _ in range(self.__NUMBEROFVEGGIES):
                        while True:
                            y = random.randint(0, width - 1)
                            x = random.randint(0, height - 1)
                            if self.__field[x][y] is None:
                                self.__field[x][y] = random.choice(self.__vegetables)
                                break
                    break
            except FileNotFoundError:
                print(f"{file_name} does not exist!")

    def initCaptain(self) -> None:
        """
        Initializes the Captain in the game.

        The method randomly selects coordinates on the game field and creates a Captain
        object at those coordinates if the location is unoccupied.

        Note:
        The Captain is a unique entity, and this method ensures that it is placed on the
        game field in an unoccupied location.
        """
        height = len(self.__field)
        width = len(self.__field[0])
        while True:
            x, y = random.randint(0, height - 1), random.randint(0, width - 1)
            if self.__field[x][y] is None:
                self.__captain = Captain(x, y)
                self.__field[x][y] = self.__captain
                break

    def initRabbits(self) -> None:
        """
        Initializes the rabbits in the game.

        The method randomly selects coordinates on the game field and creates Rabbit objects
        at those coordinates if the locations are unoccupied.

        Note:
        The number of rabbits to be initialized is determined by the __NUMBEROFRABBITS attribute.
        """
        height = len(self.__field)
        width = len(self.__field[0])
        for _ in range(self.__NUMBEROFRABBITS):
            while True:
                x, y = random.randint(0, height - 1), random.randint(0, width - 1)
                if self.__field[x][y] is None:
                    rabbit = Rabbit(x, y)
                    self.__rabbits.append(rabbit)
                    self.__field[x][y] = rabbit
                    break

    def initializeGame(self) -> None:
        """
        Initializes the entire game.

        This method calls the initVeggies, initCaptain, and initRabbits methods to set up
        the game environment with vegetables, the Captain, and rabbits.
        """
        self.initVeggies()
        self.initCaptain()
        self.initRabbits()

    def remainingVeggies(self) -> int:
        """
        Returns the number of remaining vegetables in the game.

        This method iterates over the game field and counts the number of remaining vegetables.

        Returns:
        - int: The number of remaining vegetables.
        """
        counter = 0
        for row in self.__field:
            for entity in row:
                if isinstance(entity, Veggie):
                    counter += 1
        return counter

    def intro(self) -> None:
        """
        Prints the game introduction.

        This method provides a brief welcome message to the game, explaining the objective
        to harvest vegetables before the rabbits eat them. It displays information about the
        point values of each vegetable and introduces Captain Veggie and the rabbits.

        Note:
        The vegetable information is retrieved from the __vegetables attribute.
        """
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
        """
        Prints the current state of the game field.

        This method displays the game field with its entities, including Captain Veggie,
        rabbits, and vegetables. The entities are represented by symbols, and empty spaces
        are denoted by three spaces. The entire field is enclosed by '#' characters.

        Note:
        The symbols for each entity are obtained using the getSymbol method.
        """
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
        """
        Returns the current score of the game.

        Returns:
        - int: The current score of the game.
        """
        return self.__score

    def moveSnake(self):
        if not self.__snake or not self.__captain:
            return

        directions: list[tuple[int, int]] = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ]

        snake_x = self.__snake.getX()
        snake_y = self.__snake.getY()
        captain_x = self.__captain.getX()
        captain_y = self.__captain.getY()
        target_x = snake_x
        target_y = snake_y
        min_distance = float("inf")

        for offset in directions:
            offset_x, offset_y = offset
            potential_x = snake_x + offset_x
            potential_y = snake_y + offset_y

            if 0 <= potential_x < len(self.__field) and 0 <= potential_y < len(
                self.__field[0]
            ):
                entity = self.__field[potential_x][potential_y]
                if not entity or isinstance(entity, Captain):
                    distance = (
                        abs(captain_x - potential_x) ** 2
                        + abs(captain_y - potential_y) ** 2
                    )
                    if distance <= min_distance:
                        min_distance = distance
                        target_x = potential_x
                        target_y = potential_y

        if target_x == captain_x and target_y == captain_y:
            self.__field[snake_x][snake_y] = None
            self.initSnake()
        else:
            self.__field[snake_x][snake_y] = None
            self.__snake.setX(target_x)
            self.__snake.setY(target_y)
            self.__field[target_x][target_y] = self.__snake

    def moveRabbits(self) -> None:
        """
        Moves the rabbits randomly on the game field.

        This method iterates over each rabbit in the game, randomly selects a direction
        to move, and updates the rabbit's position on the game field. If the new position
        is unoccupied or contains a vegetable, the rabbit moves; otherwise, it stays in place.
        """
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

            if 0 <= new_x < height and 0 <= new_y < width:
                if self.__field[new_x][new_y] is None or isinstance(
                    self.__field[new_x][new_y], Veggie
                ):
                    self.__field[x][y] = None
                    rabbit.setX(new_x)
                    rabbit.setY(new_y)
                    self.__field[new_x][new_y] = rabbit

    def __updateCptLocation(self, new_x: int, new_y: int) -> None:
        """
        Updates the Captain's location on the game field.

        This private method is responsible for updating the Captain's position on the game field.
        If the Captain is not initialized (None), the method does nothing.

        Parameters:
        - new_x (int): The new x-coordinate for the Captain.
        - new_y (int): The new y-coordinate for the Captain.
        """
        if self.__captain is None:
            return
        self.__field[self.__captain.getX()][self.__captain.getY()] = None
        self.__captain.setX(new_x)
        self.__captain.setY(new_y)
        self.__field[new_x][new_y] = self.__captain

    def __moveCpt(self, movement_x: int = 0, movement_y: int = 0) -> None:
        """
        Moves the Captain on the game field.

        This private method calculates the new position for the Captain based on the provided
        movement in the x and y directions. It checks if the new position is within the bounds
        of the game field and updates the Captain's location accordingly. If the new position
        is occupied by a vegetable, it adds the vegetable to the Captain's collection and updates
        the score. If the new position is occupied by a rabbit, it prints a warning message.
        If the new position is unoccupied, it updates the Captain's location.

        Parameters:
        - movement_x (int): The movement in the x-direction.
        - movement_y (int): The movement in the y-direction.
        """
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
        """
        Moves the Captain vertically on the game field.

        This method delegates the movement to the private __moveCpt method with the specified
        vertical movement.

        Parameters:
        - movement (int): The vertical movement for the Captain.
        """
        self.__moveCpt(movement_x=movement)

    def moveCptHorizontal(self, movement: int) -> None:
        """
        Moves the Captain horizontally on the game field.

        This method delegates the movement to the private __moveCpt method with the specified
        horizontal movement.

        Parameters:
        - movement (int): The horizontal movement for the Captain.
        """
        self.__moveCpt(movement_y=movement)

    def moveCaptain(self) -> None:
        """
        Moves the Captain based on user input.

        This method prompts the user to enter a direction (up, down, left, or right) and
        moves the Captain accordingly by calling the appropriate move methods.

        Note:
        The method ignores invalid input and provides feedback to the user.
        """
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
        """
        Prints the game-over message.

        This method prints a message indicating that the game is over, along with the vegetables
        harvested by the Captain and the final score.
        """
        if self.__captain is None:
            return
        print("GAME OVER!")
        print("You managed to harvest the following vegetables:")
        for v in self.__captain.getVeggies():
            print(v.getName())
        print(f"Your score was: {self.__score}")

    def highScore(self) -> None:
        """
        Records and displays the high scores.

        This method records the player's score with their initials, updates the high scores file,
        and displays the current high scores.
        """
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
