import sys
import os
import math

def getNextNumber(number):
	if (number % 2 == 0):
		return number / 2
	else:
		return 3 * number + 1

def getNumTermsInSequence(startingNumber):
	nextNumber = startingNumber
	numTerms = 1
	
	while nextNumber != 1:
		nextNumber = getNextNumber(nextNumber)
		numTerms = numTerms + 1

	return numTerms

def main():
	longestChainStartingNumber = -1
	maxTerms = -1
	
	startingNumber = 1
	for startingNumber in range(1, 1000000):
		numTerms = getNumTermsInSequence(startingNumber)
		#print("Starting at " + str(startingNumber) + ", " + str(numTerms) + " terms.")
		if (numTerms > maxTerms):
			maxTerms = numTerms
			longestChainStartingNumber = startingNumber
			
	print(str(longestChainStartingNumber) + " produced a sequence of " + str(maxTerms))
	# 837799 produced a sequence of 525
	# Elapsed time for this problem: 99.8187702627 seconds.
	
if __name__ == "__main__":
	from timeit import Timer
	t = Timer("main()", "from __main__ import main")
	print("Elapsed time for this problem: " + str(t.timeit(1)) + " seconds.")

