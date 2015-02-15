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
    x = x * 997 * 997
    x = x % 1024
    self.state = x
    return self.state

print "What is the time?"
input_string = raw_input()
print "How wide would you like the board to be?"
input_width = int(raw_input())
print "How tall would you like the board to be?"
input_height = int(raw_input())

# Take the input string and make them random.
seed = 0
for character in input_string:
  seed = seed << 1
  seed = seed ^ ord(character)

# Now make seed more random
prng = PRNG(seed)

# Create the letters list
letters = []
alphabet = map(chr, range(65, 91))
for i in range(input_width * input_height/2):
  alphabet_index = (prng.next() % 26)
  letter = alphabet[alphabet_index]
  letters.append(letter)

letters = letters + letters
#print letters

scrambled_letters = []
for i in range(len(letters)):
  scrambled_index = (prng.next() % len(letters))
  single_letter = letters.pop(scrambled_index)
  scrambled_letters.append(single_letter)

# Make the board
def chunks(l, n):
    n = max(1, n)
    return [l[i:i + n] for i in range(0, len(l), n)]

front_board = chunks(scrambled_letters, input_width)
for line in front_board:
  print line


# Make the selection board
# need to make each item a string so can pad with spaces
board_length = range(input_width * input_height)
for i in board_length:
  board_length = i.center(4, "\ ")

selection_board = chunks(range(board_length), input_width)
for line in selection_board:
  print line




# select two cards


# check if they are equal


# if they are equal, add a point. If not, unflip the cards.
