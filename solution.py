import string
import random

class Dice:
    def __init__(self):
        self._dice = []
        for i in range(6):  # dice has 6 sides.
            self._dice.append(random.choice(string.ascii_letters).upper())

class BoggleBoard:
    
    def __init__(self, size=4):
        self._size = size
        self._board = []

    def __str__(self):
        if len(self._board) == 0:
            output = ''
            for i in range(self._size):
                output += '----\n'
            return output
        else:
            for i in range(4):
                for j in range(4):
                    output += self._board[i][j]
            return output
        
new_bog = BoggleBoard()
print(new_bog)
