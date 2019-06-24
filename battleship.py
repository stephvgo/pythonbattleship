from random import randint

board = []
for x in range(0, 5):
  board.append(["O"] * 5)

def print_gameboard(board):
  for row in board:
    print " ".join(row)
print_gameboard(board)

def random_col(board):
  return randint(0, len(board[0]) - 1)

def random_row(board):
  return randint(0, len(board) - 1)

for turn in range(4):
  print "Turn", turn + 1
  guess_row = int(raw_input("To start playing, guess a row between 1 and 5:"))
  guess_col = int(raw_input("Now guess a column also between 1 and 5: "))

  if guess_row == battleship_row and guess_col == battleship_col:
    print "You win! You sank my battleship!"
    break
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print "Please enter a valid selection of rows and columns, don't waste turns!"
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
    else:
      print "You missed!"
      board[guess_row][guess_col] = "X"
    if (turn == 3):
      print "Game Over!"
  print_gameboard(board)