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

    ######################################################
    #
    # Need to check for invalid input here... If user enters
    # string, an exception is raised --> error check
    # Also, the prompt is kind of confusing. You tell the user
    # to enter option, but in what form? Int or Str? The reason
    # this is confusing is because you present it in string form
    #
    ######################################################

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

# ---> program gets hung up on anything other than option 1
# Put a print statement in the generateLetters function and you
# will realize it loops forever
board.generateLetters() 
board.assignLetterToCard()

board.printBoard()

while board.checkCards():

    ##############################################################
    #
    # What happens if user enters row and column number outside of
    # range? We get an IndexError. Also, what happens if user
    # selects a row and column that has already been chosen? 
    # You need to setup some way to determine if a slot has been 
    # chosen so that you can tell the user so --> Logic needs fixed
    #
    ##############################################################

    print("Please choose a row and a column for the 1st card")
    row = int(input("Row: "))
    column = int(input("Column: "))

    # See note mentioned above about changing card state
    choice_one = (row - 1, column - 1)
    board.changeCardState(choice_one) 
    board.printBoard()

    print("Please choose a row and a column for the 2nd card")
    row = int(input("Row: "))
    column = int(input("Column: "))

    choice_two = (row - 1, column - 1)
    board.changeCardState(choice_two)    
    board.printBoard()     
    
    ###############################################################
    # 
    # Why are you comparing the lengths of choice_one/choice_two to 2?
    # Weren't you the one who assigned them to be equal to 2? If you
    # need to check something that you did manually, then this is glaring
    # of bad program design. There is no need for that check.
    # 
    ############################################################## 
    if len(choice_one) == 2 and len(choice_two) == 2:
        match = board.compareCards(choice_one, choice_two)
    board.printBoard()

    if not match:
        board.changeCardState(choice_one)
        board.changeCardState(choice_two)
    
    board.printBoard()


########################################################################
#
#   BIGGEST TAKEAWAYS:
#       1. ERROR CHECK! ERROR CHECK! ERROR CHECK! If you want to create
#           an application that is robust and interacts with user, your 
#           program cannot break if something incorrect is entered. This 
#           aspect definitely needs to be fixed dramatically.
#       2. Better documentation! I see you made an effort with docstrings
#           in the Card class, but gave up in the Board class. The second
#           you stop documenting is the second that your code starts to
#           to become vague. I would start getting in the practice of everytime
#           you write a function to include the purpose of the function, 
#           the parameters of the function (the type and purpose), and the 
#           return value of the function. This will allow user to explicitly
#           understand your functions.
#       3. Better variable-naming. There are plenty times in your code where
#           you give a name to a variable, but it cannot be known what that
#           variable is for. If you aren't going to document, then at least
#           allow the user to understand with the naming technique.
#       4. I think you need to give the user a better experience. The prompts
#           and display are kind of vague and the user is never allowed to 
#           exit the program. This would be great if fixed.
#
########################################################################