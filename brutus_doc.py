"""
Author: Jose Eduardo Soto

Description: Reads shakespeare documents in parallel and scores the counter for 
each word. All files are stored into an array of strings. Each is a line from 
each document. The data will be decomposed into equal parts among the amount
of cores. 

"""

import pymp
import argparse
import re

#Quick setup for argparse
parser = argparse.ArgumentParser(description=
                                 'Counts all selected words in Shakespeare.')
parser.add_argument('-p', '--power', default=1, type=int,
                    help='Number of cores utilized')
args = parser.parse_args()

if (args.power < 1 or args.power > 4):
    args.power = 1

#Variable setup
filenames = []
all_lines = []
word_counter_collection = []

#set all the file names. Conveniently they're all named similarly.
for x in range(1,9):
    filenames.append('shakespeare' + str(x) + '.txt')

# Puts all lines in one large array of string lines.
for filename in filenames:
    with open(filename) as f:
        all_lines.append(f.readlines())


special_words = ['hate', 'love', 'death', 'night', 'sleep', 'sleep', 'time',
                 'henry', 'hamlet', 'you', 'hamlet', 'you', 'my', 'blood',
                 'poison', 'macbeth', 'king', 'heart', 'honest']
        
for i in range(args.power + 1):
    word_counter = {}
    for word in special_words:
        word_counter[word] = 0
    word_counter_collection.append(word_counter)

with pymp.Parallel(args.power) as p:
    partition_size = int(len(all_lines) / args.power)
    for i in p.range(args.power):
        end = len(all_lines) - 1
        if (i != (args.power-1)):
            end = (i+1) * partition_size
        for j in range((i * partition_size), end):
            array_string = ''.join(all_lines[j]).lower()
            all_lines[j] = re.split(' |\"\'.,\(\)\[]{}!?&%$#=_\n\t\r\\/~<>', array_string)
            for word in all_lines[j]:
                try:
                    word_counter_collection[i][word] += 1
                except KeyError:
                    pass


for counter in word_counter_collection:
    for key in counter:
        word_counter_collection[args.power][key] += counter[key]

print(word_counter_collection[args.power])

            
        
            

    

