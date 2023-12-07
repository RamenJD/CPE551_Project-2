from GameEngine import GameEngine


def main():
    new_game = GameEngine()
    new_game.initializeGame()
    new_game.intro()
    remaining_veggies = new_game.remainingVeggies()
    while remaining_veggies > 0:
        print(f"{remaining_veggies} veggies remaining. Current Score: {new_game.getScore()}")
        new_game.printfield()
        new_game.moveCaptain()
        new_game.moveRabbits()
        new_game.moveSnake()
        remaining_veggies = new_game.remainingVeggies()
    new_game.gameOver()


main()
