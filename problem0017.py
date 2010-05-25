import sys
import os
import math
from numpy import *

def main():
	maxNumber = 5
			#zero one two three four five six seven eight nine
	ones = [    0,  3,  3,    5,   4,   4,  3,    5,    5,   4]
	
			#zero ten twenty thirty forty fifty sixty seventy eighty ninety
	tens = [    0,  3,     6,     6,    5,    5,    5,      7,     6,     6]
	
			#ten eleven twelve thirteen fourteen fifteen sixteen seventeen eightteen nineteen
	teens = [  3,     6,     6,       8,       8,      7,      7,        9,        9,       8]
	
	sumLetters = 0
	for i in range(0, maxNumber):
		if (i < 10):
			sumLetters = sumLetters + ones[i]
		elif (i >= 10 and i < 20):
			sumLetters = sumLetters + teens[i - 10]
		elif (i >= 20 and i < 100):
			sumLetters = sumLetters + tens[i / 10] + ones[i]
		
	print("Sum of all the letters from one to " + str(maxNumber) + " is " + str(sumLetters))
	
if __name__ == "__main__":
	from timeit import Timer
	t = Timer("main()", "from __main__ import main")
	print("Elapsed time for this problem: " + str(t.timeit(1)) + " seconds.")

