import sys
import os
import math

def getNextNumber(number):
	if (number % 2 == 0):
		return number / 2
	else:
		return 3 * number + 1

#I NEVER GOT THIS TO RECURSIVE ALGORITHM TO WORK. GOT TOO COMPLICATED. STUCK WITH THE BRUTE FORCE APPROACH.
def goToNextNode(number, numTerms, validStart):
	numTerms = numTerms + 1
	
	if (2 * number > 1000000):
		topNodeNumber = goToNextNode(2 * number, numTerms, False)
	else:
		topNodeNumber = goToNextNode(2 * number, numTerms, True)
		
	if ((number - 1) % 3 == 0):
		if ((number - 1) / 3) > 1000000):
			return number
		else:
			bottomNodeNumber = goToNextNode(number - 1 / 3, numTerms, True)

			
			
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
	
if __name__ == "__main__":
	from timeit import Timer
	t = Timer("main()", "from __main__ import main")
	print("Elapsed time for this problem: " + str(t.timeit(1)) + " seconds.")

