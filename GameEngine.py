import os
import csv
import random
import pickle
from Captain import Captain
from Rabbit import Rabbit
from Veggies import Veggies
from Snake import Snake


class GameEngine:
    # Constructor
    def __init__(self):
        self.__NUMBEROFVEGGIES = 30
        self.__NUMBEROFRABBITS = 5
        self.__HIGHSCORE = 0
        self.__field = []
        self.__rabbits = []
        self.__captain = Captain(None, None)
        self.__veggies = []
        self.__snake = Snake(None, None)
        self.__score = 0
        self.__rows = 0
        self.__cols = 0

    def set_rows(self, rows):
        self.__rows = rows

    def set_cols(self, cols):
        self.__cols = cols

    def initVeggies(self):
        valid_file = False
        # Reading the prompted CSV file
        # If input file path not valid, will repeat
        while not valid_file:
            try:
                file_path = input('Please enter the name of the vegetable point file: ')
                with open(file_path, 'r') as csv_file:
                    file = csv.reader(csv_file)
                    valid_file = True
                    # Iterate over each row in the file
                    for line in file:
                        if line[0] == "Field Size":  # First row
                            # Initialize the field size based on first line
                            self.__rows = int(line[1])
                            self.__cols = int(line[2])
                            self.__field = [[None for _ in range(self.__cols)] for _ in range(self.__rows)]
                        else:  # Every other row
                            # Create a new object of the veggie: name, symbol, point
                            veggie = Veggies(line[0], line[1], int(line[2]))
                            self.__veggies.append(veggie)
            except FileNotFoundError:
                print("File path not found! Please try again.")
        # Populating veggies
        current_veggie_number = 0
        while current_veggie_number < self.__NUMBEROFVEGGIES:
            current_veggie_number += 1
            # Randomly select a veggie from the object list
            selected_veggie = random.choice(self.__veggies)
            while True:
                x_coord = random.randint(0, self.__rows - 1)
                y_coord = random.randint(0, self.__cols - 1)
                if self.__field[x_coord][y_coord] is None:  # Block is empty
                    # Add the selected veggie object to the field list
                    self.__field[x_coord][y_coord] = selected_veggie
                    break
                else:  # Block is occupied
                    continue

    def initCaptain(self):
        while True:
            x_coord = random.randint(0, self.__rows - 1)
            y_coord = random.randint(0, self.__cols - 1)
            if self.__field[x_coord][y_coord] is None:  # Block is empty
                # Set captain location
                self.__captain.set_x_coord(x_coord)
                self.__captain.set_y_coord(y_coord)
                # Update the field list
                self.__field[x_coord][y_coord] = self.__captain
                break
            else:
                continue

    def initRabbit(self):
        current_rabbit_number = 0
        while current_rabbit_number < self.__NUMBEROFRABBITS:
            current_rabbit_number += 1
            while True:
                x_coord = random.randint(0, self.__rows - 1)
                y_coord = random.randint(0, self.__cols - 1)
                if self.__field[x_coord][y_coord] is None:  # Block is empty
                    # Create a new rabbit object with the coordinates
                    rabbit = Rabbit(x_coord, y_coord)
                    # Update the rabbit list
                    self.__rabbits.append(rabbit)
                    # Update the field
                    self.__field[x_coord][y_coord] = rabbit
                    break

    def initSnake(self):
        while True:
            x_coord = random.randint(0, self.__rows - 1)
            y_coord = random.randint(0, self.__cols - 1)
            if self.__field[x_coord][y_coord] is None:  # Block is empty
                # Set captain location
                self.__snake.set_x_coord(x_coord)
                self.__snake.set_y_coord(y_coord)
                # Update the field list
                self.__field[x_coord][y_coord] = self.__snake
                print("Captain Initialized")
                break
            else:
                continue

    def initializeGame(self):
        self.initVeggies()
        self.initCaptain()
        self.initRabbit()
        self.initSnake()

    def remainingVeggies(self):
        remaining_veggies = 0
        for i in range(len(self.__field)):
            for j in range(len(self.__field[i])):
                # Check if subclass Veggies exist in field list
                if isinstance(self.__field[i][j], Veggies):
                    remaining_veggies += 1
        return remaining_veggies

    def intro(self):
        print("Welcome to Captain Veggie!")
        print("The rabbits have invaded your garden and you must harvest\n"
              "as many vegetables as possible before the rabbits eat them\n"
              "all! Each vegetable is worth a different number of points\n"
              "so go for the high score!\n")
        print("The vegetables are:")
        for i in range(len(self.__veggies)):
            print(f"{self.__veggies[i].get_symbol()}: {self.__veggies[i].get_name()} "
                  f"{self.__veggies[i].get_points()} points")
        print("Captain Veggie is \033[0;32mV\033[0m, and the rabbits are \033[0;33mR\033[0m's.\n")
        print("Good luck!")

    def printfield(self):
        print('#' * self.__cols * 3 + '#' * 2)
        for i in range(len(self.__field)):
            print('#', end='')
            for j in range(len(self.__field[i])):
                if self.__field[i][j] is None:
                    print('  ', end=' ')
                else:
                    print(f" {self.__field[i][j].get_symbol()}", end=' ')
            print('#')
        print('#' * self.__cols * 3 + '#' * 2)

    def getScore(self):
        return self.__score

    def validPos(self, current_x, current_y, moving_x, moving_y):
        if 0 <= current_x + moving_x < self.__rows and 0 <= current_y + moving_y < self.__cols:
            return True
        else:
            return False

    def moveRabbits(self):
        # Iterate through each rabbit
        for i in range(len(self.__rabbits)):
            current_x = self.__rabbits[i].get_x_coord()
            current_y = self.__rabbits[i].get_y_coord()
            moving_x = random.randint(-1, 1)
            moving_y = random.randint(-1, 1)
            # Check if moving would cause out of bound
            valid_destination = self.validPos(current_x, current_y, moving_x, moving_y)
            if valid_destination:
                # The destination is empty
                if self.__field[current_x + moving_x][current_y + moving_y] is None:
                    # Update the rabbit list
                    self.__rabbits[i].set_x_coord(current_x + moving_x)
                    self.__rabbits[i].set_y_coord(current_y + moving_y)
                    # Update the field
                    self.__field[current_x + moving_x][current_y + moving_y] = self.__rabbits[i]
                    self.__field[current_x][current_y] = None
                # The destination has veggie:
                elif isinstance(self.__field[current_x + moving_x][current_y + moving_y], Veggies):
                    # Update the rabbit's coord in the rabbit list
                    self.__rabbits[i].set_x_coord(current_x + moving_x)
                    self.__rabbits[i].set_y_coord(current_y + moving_y)
                    # Update the field by replacing the veggie with rabbit
                    self.__field[current_x + moving_x][current_y + moving_y] = self.__rabbits[i]
                    self.__field[current_x][current_y] = None
                # The destination has caption/rabbit/snake
                else:
                    continue
            # Destination is out of bound
            else:
                continue
        return

    def moveSnake(self):
        current_x = self.__snake.get_x_coord()
        current_y = self.__snake.get_y_coord()
        captain_x = self.__captain.get_x_coord()
        captain_y = self.__captain.get_y_coord()
        moving_x = 0
        moving_y = 0
        if current_x > captain_x:
            moving_x = -1
        elif current_x < captain_x:
            moving_x = 1
        else:
            if current_y > captain_y:
                moving_y = -1
            elif current_y < captain_y:
                moving_y = 1

        # The destination is empty
        if self.__field[current_x + moving_x][current_y + moving_y] is None:
            # Update Snake object's coord
            self.__snake.set_x_coord(current_x + moving_x)
            self.__snake.set_y_coord(current_y + moving_y)
            # Update field
            self.__field[current_x + moving_x][current_y + moving_y] = self.__snake
            self.__field[current_x][current_y] = None
            return
        # The destination is Captain
        elif isinstance(self.__field[current_x + moving_x][current_y + moving_y], Captain):
            print("The snake caught you. You lost last 5 veggies!")
            # If Captain has 5 or fewer than 5 veggies, empty the collection
            if len(self.__captain.Collection) <= 5:
                self.__score = 0
                self.__captain.Collection.clear()
            # If Captain has more than 5 veggies
            else:
                # Reduce points of the last 5 veggies
                for i in range(len(self.__captain.Collection) - 1, len(self.__captain.Collection) - 6, -1):
                    self.__score -= self.__captain.Collection[i].get_points()
                del self.__captain.Collection[-5:]
            # Clear Snake's position and re-initialize
            self.__field[current_x][current_y] = None
            self.initSnake()
            return
        # The destination is Veggie/Rabbit
        else:
            return

    def moveCptVertical(self, vertical):
        current_x = self.__captain.get_x_coord()
        current_y = self.__captain.get_y_coord()
        # The destination is empty
        if self.__field[current_x + vertical][current_y] is None:
            # Update the captain object's coord
            self.__captain.set_x_coord(current_x + vertical)
            # Update the field
            self.__field[current_x + vertical][current_y] = self.__captain
            self.__field[current_x][current_y] = None
            return
        # The destination is veggie
        elif isinstance(self.__field[current_x + vertical][current_y], Veggies):
            # Update the captain object's coord
            self.__captain.set_x_coord(current_x + vertical)
            veggie_found = self.__field[current_x + vertical][current_y]
            print(f"Yummy! A delicious {veggie_found.get_name()}")
            self.__captain.addVeggie(veggie_found)
            self.__score += veggie_found.get_points()
            # Update the field
            self.__field[current_x + vertical][current_y] = self.__captain
            self.__field[current_x][current_y] = None
            return
        # The destination is rabbit/snake
        else:
            return

    def moveCptHorizontal(self, horizontal):
        current_x = self.__captain.get_x_coord()
        current_y = self.__captain.get_y_coord()
        # The destination is empty
        if self.__field[current_x][current_y + horizontal] is None:
            # Update the captain object's coord
            self.__captain.set_y_coord(current_y + horizontal)
            # Update the field
            self.__field[current_x][current_y + horizontal] = self.__captain
            self.__field[current_x][current_y] = None
            return
        # The destination is veggie
        elif isinstance(self.__field[current_x][current_y + horizontal], Veggies):
            # Update the captain object's coord
            self.__captain.set_y_coord(current_y + horizontal)
            veggie_found = self.__field[current_x][current_y + horizontal]
            print(f"Yummy! A delicious {veggie_found.get_name()}")
            self.__captain.addVeggie(veggie_found)
            self.__score += veggie_found.get_points()
            # Update the field
            self.__field[current_x][current_y + horizontal] = self.__captain
            self.__field[current_x][current_y] = None
            return
        # The destination is rabbit/snake
        else:
            return

    def moveCaptain(self):
        current_x = self.__captain.get_x_coord()
        current_y = self.__captain.get_y_coord()
        direction = input("Would you like to move up(W), down(S), left(A), or right(D): ")
        if direction == "W" or direction == "w":
            valid_destination = self.validPos(current_x, current_y, -1, 0)
            if valid_destination:
                self.moveCptVertical(-1)
            return
        elif direction == "S" or direction == "s":
            valid_destination = self.validPos(current_x, current_y, 1, 0)
            if valid_destination:
                self.moveCptVertical(1)
            return
        elif direction == "A" or direction == "a":
            valid_destination = self.validPos(current_x, current_y, 0, -1)
            if valid_destination:
                self.moveCptHorizontal(-1)
            return
        elif direction == "D" or direction == "d":
            valid_destination = self.validPos(current_x, current_y, 0, 1)
            if valid_destination:
                self.moveCptHorizontal(1)
        else:
            print(f"{direction} is not a valid option")

    def gameOver(self):
        print("GAME OVER!")
        print("You managed to harvest the following vegetables:")
        for i in range(len(self.__captain.Collection)):
            print(self.__captain.Collection[i].get_name())
        print(f"Your score was: {self.getScore()}")

    def highScore(self):
        highscores = []
        player_name = input("Please enter your three initials to go on the scoreboard: ")
        player_info = (player_name, self.getScore())
        if os.path.exists("highscore.data"):
            # Unpickle highscore.data
            with open("highscore.data", "rb") as inFile:
                highscores = pickle.load(inFile)
                inserted = False
                for i in range(len(highscores)):
                    # If player's score is higher than any of the existing score
                    if highscores[i][1] < player_info[1]:
                        highscores.insert(0, player_info)
                        inserted = True
                        break
                if not inserted:
                    highscores.append(player_info)
        else:
            highscores.append(player_info)
        # Output all the high scores
        print("-----HIGH SCORES-----\n"
              "Name\t\tScore")
        for i in range(len(highscores)):
            print(f"{highscores[i][0]}\t{highscores[i][1]}")
        # Pickle highscore.data
        with open("highscore.data", "wb") as outFile:
            pickle.dump(highscores, outFile)
