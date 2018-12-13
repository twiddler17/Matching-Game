from card import Card
import random

class Board:
    
<<<<<<< HEAD
=======
    #########################################################
    #
    # I think 'self._side' could be a little clearer. Without 
    # investigating, it is not clear what that variable represents
    # Just as well, there is no documentation stating what it is.
    # If you are not going to document it, you better make sure 
    # the purpose is explicit.
    #
    #########################################################
>>>>>>> 41ff3babf9c4294a23f679bd75282d1291276135
    def __init__(self, side):
        """Constructor"""
        self._side = side
        self._board = [[0] * self._side for row in range(self._side)]
        self._letters = {}

    @property
    def board(self):
        """Getter"""
        return self._board

    # def addItem(self, side, card):
    #     """Assigns a Card object to an element in the two dimensional list"""
    #     if side >= 0 and side < self._side:
    #         if side >= 0 and side < self._side:
    #             self._board[row][column] = card                

    def printBoard(self):
        print("---------------------------")
        for row in range(self._side):
            for column in range(self._side):
                    print(self._board[row][column].showCard(), end = ' ')
            print()

    def getCard(self, side):
        return self._board[side][side].letter

    def compareCards(self, choice_one, choice_two):
        row_one, column_one = choice_one
        row_two, column_two = choice_two

        if self._board[row_one][column_one].letter == self._board[row_two][column_two].letter:
            return True
        else:
            return False

    def generateLetters(self):
        number_letters = self._side * self._side
        self._letters = {}
        while len(self._letters) < number_letters / 2:
            letter = random.randrange(65, 91)
            if letter not in self._letters:
                self._letters[letter] = 2

    def assignLetterToCard(self):
        temp_letters = self._letters
        while len(temp_letters) > 0:
            for row in range(self._side):
                for column in range(self._side):
                    number = random.choice(list(temp_letters.keys()))
                    card = Card(number)
                    self._board[row][column] = card
                    if temp_letters[number] == 2:
                        temp_letters[number] -= 1
                    else:
                        temp_letters.pop(number)
    
    def checkCards(self):
        all_closed = True
        for row in range(self._side):
            if all_closed:
                break
            for column in range(self._side):
                if all_closed:
                    break
                all_closed = self._board[row][column].isClosed()
        return all_closed

    def changeCardState(self, choice):
        row, column = choice
        if self._board[row][column].isClosed():
            self._board[row][column].openCard()
        else:
            self._board[row][column].closeCard()
