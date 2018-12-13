class Card:
    
    def __init__(self, letter = 48):
        """Constructor"""
        self._letter = str(chr(letter))
        self._closed = True

    @property
    def letter(self):
        """Getter"""
        return self._letter

    @letter.setter
    def letter(self, letter):
        """Setter"""
        if letter >= 65 and letter <= 90:
            self._letter = str(chr(letter))
        else:
            raise ValueError("Letter is outside of valid range")

    def isClosed(self):
        """Returns True if card is closed"""
        return self._closed

    def openCard(self):
        """Changes the state of the card to Open"""
        self._closed = False

    def closeCard(self):
        self._closed = True

    def showCard(self):
        """Return value or "*" depending on the state (closed variable)

        Use this function in most cases
        """
        return self._letter if self._closed == False else "*"


    




