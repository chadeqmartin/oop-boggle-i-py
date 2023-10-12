import random
import string

class BoggleBoard:
  
  def __init__(self, size=4):
    self.size = size
    self.board = []

  def __str__(self):
    return f"{self.board[0]}\n {self.board[1]}\n {self.board[2]}\n {self.board[3]}"

  def shake(self):
    alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    all_rows = []
    for rows in range(self.size):
      for letters in range(self.size):
        random.shuffle(alpha)
        current_row = alpha[0:4]
      all_rows.append(current_row)
      
    for row in all_rows:
        print(" ".join(row))

    self.board[len(self.board)] = all_rows
    print(self.board)
    return 

if __name__ == '__main__':
  new_board = BoggleBoard()
  print(new_board.size)
  # print(new_board.board)
  # print(new_board.shake)
  print(new_board)
  #print(display_board())
  # print(display_board)
  # print(1)
  # initialize board
  # display empty board
  # prompt for shake 
  # if shake == True
  # board_obj.shake
  # print(first_four)
  # user = BoggleBoard()
  # print(user.display_board)
