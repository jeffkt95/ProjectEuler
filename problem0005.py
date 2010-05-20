import sys
import os
import math

def main():
	highestNumber = 20
	maxCheck = highestNumber * 100000000
	
	# Starting with highestNumber, go up by multiples of highestNumber
	# e.g. if your highestNumber was 10, check 10, 20, 30, 40, etc.
	for numForCheck in range(highestNumber, maxCheck, highestNumber): 
		#Assume it's evenly divisible by all until proven otherwise
		evenlyDivisibleByAll = True
		for i in range(highestNumber, 0, -1):
			if numForCheck % i != 0:
				evenlyDivisibleByAll = False
				break
		
		#If you get through all the numbers and evenlyDivisibleByAll is still true,
		#  then you've found the answer
		if evenlyDivisibleByAll:
			print(str(numForCheck) + " is evenly divisible by all numbers from 1 to " + str(highestNumber))
			return
	
	print("Unable to find any number evenly divisible by all numbers from 1 to " + str(highestNumber))
	print("I checked up to " + str(maxCheck))
		
if __name__ == "__main__":
	main()

