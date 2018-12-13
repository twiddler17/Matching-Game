import random
from card import Card
from board import Board
import time

BOARD_ONE = 4
BOARD_TWO = 6
BOARD_THREE = 8

#Begin

choice = -1

while choice < 1 or choice > 3:
    print("!!!Match the letters!!!")
    print("Option 1: 4x4")
    print("Option 2: 6x6")
    print("Option 3: 8x8")
    choice = int(input("Enter Option: "))
    if choice == 1:
        board = Board(BOARD_ONE)
    elif choice == 2:
        board = Board(BOARD_TWO)
    elif choice == 3:
        board = Board(BOARD_THREE)

board.generateLetters()
board.assignLetterToCard()

board.printBoard()

while board.checkCards():
    print("Please choose a row and a column for the 1st card")
    row = int(input("Row: "))
    column = int(input("Column: "))

    choice_one = (row - 1, column - 1)
    board.changeCardState(choice_one) 
    board.printBoard()

    print("Please choose a row and a column for the 2nd card")
    row = int(input("Row: "))
    column = int(input("Column: "))

    choice_two = (row - 1, column - 1)
    board.changeCardState(choice_two)    
    board.printBoard()     
    
    if len(choice_one) == 2 and len(choice_two) == 2:
        match = board.compareCards(choice_one, choice_two)
    board.printBoard()

    if not match:
        board.changeCardState(choice_one)
        board.changeCardState(choice_two)
    
    board.printBoard()

