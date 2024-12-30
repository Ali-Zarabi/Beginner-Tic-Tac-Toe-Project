"""
Ali Zarabi - Tic Tac Toe Console Game:
"""

import os  # Import os to be able to clear the screen
import time  # Import time to be able to have pauses for user experience
import random  # Import random to be able to create a random choice for the bot

"""VARIABLES"""
# Set a variable to capture the string containg the play methods of the game
howto = """
Tic Tac Toe - How To Play:

Welcome to Tic Tac Toe. The game is very straightforwards. You and another player,
either a friend or a bot, both take turns placing your symbol, X or O. Whoever gets
three in a row either vertically, horizontally, or diagonally wins !
"""

# Set a variable to set a condition for the first run of the game
firstrun = True

# Set variables to suffice the conditions of the game menu loop
gameloop = True
"""FUNCTIONS"""


def game(players):  # Define a function for the core game logic
    # Create a list representing all available spaces on the board
    squares = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    # Create a variable for whether you are in the game or not
    gamestate = True
    count = 0  # Create a variable for the number of elapsed turns
    turn = 0  # Create a varible to check which players turn it is
    while gamestate == True:
        # Code for single player:
        if players == "1":
            while turn == 0:
                print(updateboard(squares))  # Print the board
                # Take a placement input
                place1 = input("Player - Pick Your Square : ")
                if not place1 in squares:  # Only accept available spaces
                    print("Invalid input, try again")
                else:
                    for x in range(len(squares)):
                        # Replace the variable for the chosen place with
                        # an X to indicate the players choice
                        if squares[x] == place1:
                            squares[x] = "X"
                            print(updateboard(squares))
                            # Update who's turn it is and elapsed turns
                            turn = 1
                            count += 1

            winstate = checkwin(squares)  # Run a function to see if anyone won
            # If player 1 wins, print the win, append to the history file
            # and end the gameplay loop
            if winstate == True and turn == 1:
                print("Player 1 Wins !")
                gamestate = False
                historyappend(players, turn, updateboard(squares))
                turn = 3

            # If the total maximum amount of turns have passed and nobody's won,
            # print that it's a tie. Append this to the play history file.
            if count == 9 and winstate == None:
                print("It's A Tie !")
                gamestate = False
                turn = 3
                historyappend(players, turn, updateboard(squares))
            # If it's the bot's turn, assign its choice to a random index of the list
            while turn == 1:
                botturn = random.randint(0, 8)
                # If that index is unavailable, find another that is free
                while squares[botturn] == "X" or squares[botturn] == "O":
                    botturn = random.randint(0, 8)
                # Change that space to O and print user experience loading time
                squares[botturn] = "O"
                print("Choosing", end="\r")
                time.sleep(0.75)
                print("Choosing.", end="\r")
                time.sleep(0.75)
                print("Choosing..", end="\r")
                time.sleep(0.75)
                print("Choosing...", end="\r")
                time.sleep(1)
                # Update who's turn it is and elapsed turns
                turn = 0
                count += 1
            # Check if the bot wins. Print the win, append to the play history
            # file and end the game loop if so
            winstate = checkwin(squares)
            if winstate == True and turn == 0:
                print(updateboard(squares))
                print("Bot Wins !")
                gamestate = False
                historyappend(players, turn, updateboard(squares))
                turn = 3
        # Code for two players:
        if players == "2":
            print(updateboard(squares))
            # If it's player 1's turn, take a space input
            while turn == 0:
                place1 = input("Player 1 - Pick Your Square : ")
                if not place1 in squares:
                    print("Invalid input, try again")
                else:
                    # Change that space to print X
                    for x in range(len(squares)):
                        if squares[x] == place1:
                            squares[x] = "X"
                            print(updateboard(squares))
                            # Update who's turn it is and elapsed turns
                            turn = 1
                            count += 1

            # Check if Player 1 wins. Print the win, append to the play history
            # file and end the game loop if so.
            winstate = checkwin(squares)
            if winstate == True and turn == 1:
                print("Player 1 Wins !")
                gamestate = False
                historyappend(players, turn, updateboard(squares))
                turn = 3
            # If the max amount of turns is reached and nobody has won, confirm
            # a tie, append to the play history file and end the game loop.
            if count == 9 and winstate == None:
                print("It's A Tie !")
                gamestate = False
                turn = 3
                historyappend(players, turn, updateboard(squares))
            # If it's player 2's turn, take their space input
            while turn == 1:
                place2 = input("Player 2 - Pick Your Square : ")
                if not place2 in squares:
                    print("Invalid input, try again")
                else:
                    # Change their corresponding place input to O
                    for x in range(len(squares)):
                        if squares[x] == place2:
                            squares[x] = "O"
                            # Update who's turn it is and elapsed turns
                            turn = 0
                            count += 1

            # Check if Player 2 wins. Print the win, append to the play history
            # file and end the game loop if so.
            winstate = checkwin(squares)
            if winstate == True and turn == 0:
                print(updateboard(squares))
                print("Player 2 Wins !")
                gamestate = False
                historyappend(players, turn, updateboard(squares))
                turn = 3


# Function that checks if any win condition is true, returning true if so
def checkwin(board):
    if (
        board[0] == board[3] == board[6]
        or board[1] == board[4] == board[7]
        or board[2] == board[5] == board[8]
        or board[0] == board[1] == board[2]
        or board[3] == board[4] == board[5]
        or board[6] == board[7] == board[8]
        or board[0] == board[4] == board[8]
        or board[2] == board[4] == board[6]
    ):
        return True


# Function that returns the updated board with all user inputs present
def updateboard(squares):
    board = f"""
      |     |
   {squares[0]}  |  {squares[1]}  |  {squares[2]}
 _____|_____|_____
      |     |
   {squares[3]}  |  {squares[4]}  |  {squares[5]}
 _____|_____|_____
      |     |
   {squares[6]}  |  {squares[7]}  |  {squares[8]}
      |     |
      """
    return board


# Function that checks the number of players, the winner and the final playing
# board and writes that to the .txt file
def historyappend(players, winner, board):
    if winner == 1:
        winner = "Player 1"
    elif winner == 0:
        if players == 1:
            winner = "Bot"
        else:
            winner = "Player 2"
    else:
        winner = "N/A - Tie"
    with open("History.txt", "a") as file:
        file.write(
            f"""
Players: {players} - Winner: {winner}
           
            {board}\n
           """
        )


"""PROGRAM BODY"""
os.system("cls")
# Run the introdution program if the file was just opened
if firstrun == True:
    print(
        """
To best experience this code, please enlarge the console.
          """
    )
    input("\nPress enter to continue... ")
    os.system("cls")
    print(howto)
    time.sleep(12)
    firstrun = False  # Declare that it is no longer the first run

while gameloop == True:  # Set a loop to run until the user exits
    # Print the menu and it's options
    print(
        """
         _______ _         _______            _______
        |__   __(_)       |__   __|          |__   __|
           | |   _  ___      | | __ _  ___      | | ___   ___
           | |  | |/ __|     | |/ _` |/ __|     | |/ _ \ / _ \

           | |  | | (__      | | (_| | (__      | | (_) |  __/
           |_|  |_|\___|     |_|\__,_|\___|     |_|\___/ \___|

      _____ _             _         _____  _
     / ____(_)           | |       |  __ \| |
    | (___  _ _ __   __ _| | ___   | |__) | | __ _ _   _  ___ _ __
     \___ \| | '_ \ / _` | |/ _ \  |  ___/| |/ _` | | | |/ _ | '__|
     ____) | | | | | (_| | |  __/  | |    | | (_| | |_| |  __| |
    |_____/|_|_| |_|\__, |_|\___|  |_|    |_|\__,_|\__, |\___|_|
                     __/ |                          __/ |
                    |___/                          |___/
          _______               _____  _
         |__   __|             |  __ \| |
            | __      _____    | |__) | | __ _ _   _  ___ _ __
            | \ \ /\ / / _ \   |  ___/| |/ _` | | | |/ _ | '__|
            | |\ V  V | (_) |  | |    | | (_| | |_| |  __| |
            |_| \_/\_/ \___/   |_|    |_|\__,_|\__, |\___|_|
                                               __/ |
                                              |___/
      _____  _                _    _ _     _
     |  __ \| |              | |  | (_)   | |
     | |__) | | __ _ _   _   | |__| |_ ___| |_ ___  _ __ _   _
     |  ___/| |/ _` | | | |  |  __  | / __| __/ _ \| '__| | | |
     | |    | | (_| | |_| |  | |  | | \__ | || (_) | |  | |_| |
     |_|    |_|\__,_|\__, |  |_|  |_|_|___/\__\___/|_|   \__, |
                      __/ |                               __/ |
                     |___/                               |___/
                       ______      _ _
                      |  ____|    (_| |
                      | |__  __  ___| |_
                      |  __| \ \/ | | __|
                      | |____ >  <| | |_
                      |______/_/\_|_|\__|

               """
    )
    players = input(
        "[1]: Single Player - [2]: Two Player - [H]: Play History - [E]: Exit : "
    ).lower()
    if players == "1" or players == "2":
        game(players)  # Run the game function
    elif players == "e":
        gameloop = False  # End the while loop if the user chooses to exit
    elif players == "h":  # Open, read, and print the play history file
        with open("History.txt", "r") as file:
            history = file.read()
            # If the file is blank, print that there is no play history
            if history == "":
                print("There is no play history")
                input("Press enter to continue... ")
            else:
                print(history)
                input("Press enter to continue... ")
    else:
        print("Invalid input, please try again.", end="\r")

# Print the closing code and terminate the program
print("Sorry to see you leave.", end="\r")
time.sleep(3)
print("                                ", end="\r")
print("Until next time!")
