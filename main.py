#!/usr/bin/python

######################################################
########### card-flip memory game ####################

class PRNG(object):
  def __init__(self, seed):
    self.state = seed

  def next(self):
    x = self.state
    x = x + 1
    x = x << 8 | x >> 8
    x = x * 997
    x = x % 998
    self.state = x
    return self.state

# todo: ask user for time
# todo: convert time to integer
# todo: pass PRNG integer to seed the random number generator
prng = PRNG(0)

for i in range(10):
  print prng.next()

# initialize the board with a make_board function
#def chunks(l, n):
#    n = max(1, n)
#    return [l[i:i + n] for i in range(0, len(l), n)]

#def card_front(board_width, board_length):
#  letters = map(chr, range(65, 91))
#  board_letters = random.sample(letters, board_width*board_length/2)*2
#  scrambled_board = random.sample(board_letters, len(board_letters))
#  board = np.matrix(chunks(scrambled_board, board_width))
#  print board

#myboard = card_front(4,4)
#print myboard

# select two cards




# check if they are equal




# if they are equal, add a point. If not, unflip the cards.
