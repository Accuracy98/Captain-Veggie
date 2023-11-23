# Author: Zhekang Xu
# Date: 2023-11-22
# Description: main functions, the enter of program main functions, the enter of program

from GameEngine import GameEngine


def main():
    game_engine = GameEngine()
    game_engine.initVeggies()
    game_engine.initCaptain()
    game_engine.initRabbits()
    game_engine.initSnake()
    game_engine.intro()
    remaining_vegetables = game_engine.remainingVeggies()
    while remaining_vegetables != 0:
        print(
            f"{remaining_vegetables} veggies remaining. Current score: {game_engine.getScore()}"
        )
        game_engine.printField()
        game_engine.moveRabbits()
        game_engine.moveCaptain()
        game_engine.moveSnake()
        remaining_vegetables = game_engine.remainingVeggies()

    game_engine.gameOver()
    game_engine.highScore()


if __name__ == "__main__":
    main()
