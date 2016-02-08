#!usr/bin/env python

import os
import sys
wordFile = sys.argv[1]
words = open(wordFile, 'r').read()
wordstring = words.replace('\n', ' ')
wordlist = wordstring.split(' ')
print len(wordlist)
##return len(wordlist)

