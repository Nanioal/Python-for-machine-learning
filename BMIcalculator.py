import random

def validinput(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Error: Please enter a positive integer value.")
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")

# Prompt user for grid size
rows = validinput("Specify the number of rows of your board to be in nxm: ")
columns = validinput("Specify the number of columns of your board to be in nxm: ")

def treasureplacement(prompt, max_value):
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= max_value:
                return value - 1  # Adjust for 0-based indexing
            else:
                print(f"Error: Please enter a value between 1 and {max_value}.")
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")

def acceptHiddenPlace(max_rows, max_columns):
    rowHide = treasureplacement("In which row do you want to hide your treasure (1-based index): ", max_rows)
    columnHide = treasureplacement("In which column do you want to hide your treasure (1-based index): ", max_columns)
    return rowHide, columnHide

def placeTrap(rows, columns, treasureRow, treasureCol):
    while True:
        trapRow = random.randint(0, rows - 1)
        trapCol = random.randint(0, columns - 1)
        if trapRow != treasureRow or trapCol != treasureCol:
            return trapRow, trapCol

def createGrid(rows, columns, treasureRow, treasureCol, trapRow, trapCol):
    for i in range(rows):
        for j in range(columns):
            if i == treasureRow and j == treasureCol:
                print('T', end=' ')
            elif i == trapRow and j == trapCol:
                print('X', end=' ')
            else:
                print('*', end=' ')
        print()  # Newline after each row

def playerGuess(rows, columns, treasureRow, treasureCol, trapRow, trapCol):
    while True:
        guessRow = treasureplacement("Guess the row of the treasure (1-based index): ", rows)
        guessCol = treasureplacement("Guess the column of the treasure (1-based index): ", columns)

        if guessRow == treasureRow and guessCol == treasureCol:
            print("Congratulations! You found the treasure!")
            break
        elif guessRow == trapRow and guessCol == trapCol:
            print("Oh no! You fell into a trap! Game over.")
            break
        else:
            print("Not here. Try again!")

# Example usage
treasureRow, treasureCol = acceptHiddenPlace(rows, columns)
trapRow, trapCol = placeTrap(rows, columns, treasureRow, treasureCol)
playerGuess(rows, columns, treasureRow, treasureCol, trapRow, trapCol)
createGrid(rows, columns, treasureRow, treasureCol, trapRow, trapCol)
