#!usr/bin/env python
import random
import string
wordlist = open('/usr/share/dict/words', 'r').read()
wordList = wordlist.split(' ')
wordList = [x.replace('\n', '') for x in wordList]
words = ''

for i in range(750):
    newWord = ''
    newWord += random.choice(wordList)
    words += 'Matt'
    words += ' '
wordFile = open('testwords.txt', 'w')
wordFile.write(words)
wordFile.close()


