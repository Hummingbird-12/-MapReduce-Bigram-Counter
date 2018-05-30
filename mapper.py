#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sys import stdin, stdout

while True:
    inp = stdin.readline() # read single line from input
    if inp == "": # check for empty input string
        break # end loop

    words = inp.strip().split() # strip line and split into list of words

    for index in range(1, len(words)): # for each word in line
        stdout.write("%s %s\t1\n" %(words[index - 1], words[index])) # output to stdout
