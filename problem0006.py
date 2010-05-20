import sys
import os
import math

def main():
	highestNumber = 100

	sumSquares = 0
	sum = 0
	for i in range(1, highestNumber+1):
		sum = sum + i
		sumSquares = sumSquares + i * i
		
	squareSum = sum * sum
	
	difference = squareSum - sumSquares
	print("Difference is " + str(difference))
		
if __name__ == "__main__":
	main()

