#!usr/bin/env python
import random
import string
wordList = open('/usr/share/dict/words', 'r').read()
wordList = wordList.split('\n')
wordList = [x.replace('\n', ' ') for x in wordList]
words = ''

for i in range(750):
    newWord = ''
    newWord += random.choice(wordList)
    words += newWord
    words += ' '
wordFile = open('testwords.txt', 'w')
wordFile.write(words)
wordFile.close()


