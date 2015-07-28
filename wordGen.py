#!usr/bin/env python
import random
import string

words = ''
for i in range(125):
    newWord = ''
    for e in range(random.randrange(0,15)):
        newWord += random.choice(string.ascii_letters)
    words += newWord
    words += ' '
wordFile = open('testwords.txt', 'w')
wordFile.write(words)
wordFile.close()


