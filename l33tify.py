#!/usr/bin/env python
# -*- coding: latin-1 -*-

import sys
import random

# dict for l33t-sp33k
l33t_dic = {	"a":"@",	"b":"8",	"c":"(",	"d":"|)",	"e":"€",
				"f":"|=",	"g":"9",	"h":"|-|",	"i":"|",	"j":"_|",
				"k":"|<",	"l":"|_",	"m":"|\/|",	"n":"|\|",	"o":"0",
				"p":"|D",	"q":"(,)",	"r":"®",	"s":"$",	"t":"+",
				"u":"|_|",	"v":"\/",	"w":"\/\/",	"x":"><",	"y":"`/",
				"z":"2"		}

# function to scramble a word
def scramble(inString):
	output = ""
	for char in inString:
		r = random.random()
		# only replace 30% of letters
		if l33t_dic.has_key(char.lower()) == False or r > 0.3:
			output += char
			continue
		output+= l33t_dic.get(char.lower())

	return output

# do the things
inputStrings = sys.argv[1:]
out = ""
for inputString in inputStrings:
	scram = scramble(inputString)
	out += scram+" "

out = out.strip();

print "Scrambled version:"
print out
