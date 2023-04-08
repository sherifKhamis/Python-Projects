# Sudoku Game in Python

import numpy as np
import random


def generateGame(difficulty):

    global board
    board = np.zeros((9, 9), dtype=int)
    for rows in range(9):
        for columns in range(9):
            randomNumber = random.randrange(1, 10)
            if random.randrange(difficulty) == 0:
                board[rows][columns] = 0
                continue
            while not noRep(rows, columns, randomNumber):
                randomNumber = random.randrange(1, 10)
            board[rows][columns] = randomNumber


def noRep(rows, columns, number):

    # No repetition in rows
    for column in board[rows]:
        if column == number:
            return False

    # No repetition in columns
    for x in range(9):
        field = board[x][columns]
        if field == number:
            return False

    # No repetition in square
    for y in range(3):
        for z in range(3):
            if board[y+int(rows/3)*3][z+int(columns/3)*3] == number:
                return False

    # If no repetition found return True
    return True


def menu():

    print("Welcome to Sudoku in Python")
    print("\nWhich difficulty do you want to play ?")
    print("a) EASY b) MEDIUM c) HARD")
    difficulty = input("Choice: ")
    difficultyDict = {"a": 6, "b": 4, "c": 2}
    generateGame(difficultyDict[difficulty])


menu()

