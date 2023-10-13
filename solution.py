import string
from itertools import repeat
import random

class Dice:
    def __init__(self):
        self._dice = []
        for i in range(6):  # dice has 6 sides.
            self._dice.append(random.choice(string.ascii_letters).upper())

class BoggleBoard:

    def __init__(self, row_size=4, board_length=4):
        self._row_size = row_size
        self._board_length = board_length
        self._board = []

        for i in range(self._board_length):
            row = list(repeat("_", self._row_size))
            self._board.append(row)

    def __str__(self):
        output = ''
        for i in range(self._board_length):
            for j in range(self._row_size):
                output += self._board[i][j]
            output += "\n"
        return output
    
    
    def shake(self):
        for i in range(self._board_length):
            for j in range(self._row_size):
                each_dice = Dice()
                dice_roll = random.choice(each_dice._dice)
                self._board[i][j] = dice_roll + "  "
                if self._board[i][j] == "Q  ":
                    self._board[i][j] = "Qu "
    
new_bog = BoggleBoard()
print(new_bog)
new_bog.shake()
print(new_bog)
