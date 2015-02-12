#!/usr/bin/python

######################################################
########### card-flip memory game ####################

# dependencies
import random
import numpy as np


# initialize the board
letters = map(chr, range(65, 91))
board_width = 4
board_length = 4
board_letters = random.sample(letters, board_width*board_length/2)*2
#print board_letters
scrambled_board = random.sample(board_letters, len(board_letters))
#print scrambled_board

def chunks(l, n):
    n = max(1, n)
    return [l[i:i + n] for i in range(0, len(l), n)]

board = np.matrix(chunks(scrambled_board, board_width))
print board

# select two cards




# check if they are equal




# if they are equal, add a point. If not, unflip the cards.