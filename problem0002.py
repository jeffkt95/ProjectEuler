import sys
import os
import math

def main():
	sequence0 = 1
	sequence1 = 2
	sum = 0
	while sequence1 < 4000000:
		# add the last two to the sum if they are even
		if sequence1 % 2 == 0:
			sum = sum + sequence1
			
		sequenceNew1 = sequence0 + sequence1
		sequence0 = sequence1
		sequence1 = sequenceNew1
	
	print("Sum of all the evens up to 4 milion: " + str(sum))
	
if __name__ == "__main__":
	main()

