#!usr/bin/env python
import random
wordList = open('motherFile.txt', 'r').read()
wordList = wordList.split(' ')
wordList = [x.replace('\n', ' ') for x in wordList]
words = ''
seed = random.choice(range(len(wordList)))
for i in range(75):
    newWord = ''
    newWord += wordList[seed+i]
    words += newWord
    words += ' '
wordFile = open('seedWords.txt', 'w')
wordFile.write(words)
wordFile.close()


