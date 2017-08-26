#!/usr/bin/env python

from random import shuffle
import sys

# function to scramble a word
def scramble(inString):
	result = inString[0]
	innards = list(inString[1:-1])
	if len(inString) == 1:
		return inString
	
	# construct output
	while(True):
		shuffle(innards)
		result = inString[0]
		for innard in innards:
			result += innard
		result += inString[-1]
		
		# if output happens to match input, try it again
		if (len(inString) < 4 or result != inString):
			break
		else:
			result = inString[0]
	return result

# do the things
inputStrings = sys.argv[1:] 
out = ""
for inputString in inputStrings:
	scram = scramble(inputString)
	out += scram+" "

out = out.strip();

print "Scrambled version:"
print out
