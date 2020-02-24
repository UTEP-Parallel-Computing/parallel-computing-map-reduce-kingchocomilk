"""
Author: Jose Eduardo Soto

Description: Reads shakespeare documents in parallel and scores the counter for 
each word. All files are stored into an array of strings. Each is a line from 
each document. The data will be decomposed into equal parts among the amount
of cores. 

"""

import pymp
import argparse

#Quick setup for argparse
parser = argparse.ArgumentParser(description=
                                 'Counts all selected words in Shakespeare.')
parse.add_arguement('-p', '--power', default=1, type=int,
                    help='Number of cores utilized')
args = parser.parse_args()

if (args.power < 1 or args.power > 4):
    args.power = 1

#Variable setup
filenames = []
all_lines = []

#set all the file names. Conveniently they're all named similarly.
for x in range(1,9):
    filenames.append('shakespeare' + x + '.txt.')

# Puts all lines in one large array of string lines.
for filename in filenames:
    with open(filename) as f:
        all_lines.append(f.readlines())

special_words = ['hate', 'love', 'eath', 'night', 'sleep', 'sleep', 'time',
                 'henry', 'hamlet', 'you', 'hamlet', 'you', 'my', 'blood',
                 'poison', 'macbeth', 'king', 'heart', 'honest']
        
def index(n):
    return all_lines[n]

class ShakespeareReader:

    word_counter = {}

    def __init__(self):
        for word in special_words:
            word_counter[word] = 0

    def read_word(self, considered_word):
        try:
            word_counter[considered_word]
            

    

