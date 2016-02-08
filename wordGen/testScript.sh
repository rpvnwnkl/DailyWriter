#!/bin/bash

python seedGen.py
#create seed excerpt from previous diary writings

theSeed=$(<~/OneDrive/Python/DailyWriter/wordGen/seedWords.txt)
#save seed excerpt to local variable

cd char-rnn/
#nav into char dir to make th work right

th sample.lua cv/lm_lstm_epoch50.00_1.0460.t7 -length 5000 -verbose 0 -temperature 0.5 -primetext "$theSeed" > ~/OneDrive/Python/DailyWriter/wordGen/tempWords.txt
#execute char script with seed primer and med temperature, save file to tempWords.txt


