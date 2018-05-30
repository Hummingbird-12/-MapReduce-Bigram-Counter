#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sys import stdin, stdout

bigram = {} # dictionary to store bigram count

while True:
    inp = stdin.readline() # read single line from input
    if inp == "": # check for empty input string
        break # end loop

    comb, n = inp.strip().split("\t") # store bigram in comb and number in n
    if comb not in bigram: # check if bigram exists in dictionary
        bigram[comb] = 0 # create key with value of 0
    bigram[comb] += 1 # increase value by 1

for entry in sorted(list(bigram.keys())): # for each key of dictionary sorted
    stdout.write("%s\t%d\n" %(entry, bigram[entry])) # output bigram count to stdout
