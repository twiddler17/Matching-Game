class Card:
    
<<<<<<< HEAD
    def __init__(self, letter = 48):
        """Constructor"""
=======
    ###################################################
    #
    # Dont put space in between keyword arg and assignment
    # letter = 48 should be letter=48
    #
    ####################################################
    def __init__(self, letter = 48):
        """Constructor"""
        
>>>>>>> 41ff3babf9c4294a23f679bd75282d1291276135
        self._letter = str(chr(letter))
        self._closed = True

    @property
    def letter(self):
        """Getter"""
<<<<<<< HEAD
        return self._letter

=======
        
        return self._letter

    #####################################################
    #
    # I think this function may need to be adjusted a litte
    # We will look at it later. Docstrings need work
    #
    #####################################################
>>>>>>> 41ff3babf9c4294a23f679bd75282d1291276135
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
<<<<<<< HEAD
=======

        ######################################################
        #
        # I prefer the following:
        #       return self._letter if not self._closed else "*"
        # Not that the way you wrote it was wrong, but I think
        # the former is more clear to developers
        #
        ######################################################
>>>>>>> 41ff3babf9c4294a23f679bd75282d1291276135
        return self._letter if self._closed == False else "*"


    




