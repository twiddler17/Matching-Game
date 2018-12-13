from card import Card
import random

class Board:
    
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
                for column in range(self._side):1