import sys
import os
import math

def main():
	numberToCheck = 600851475143
	
	for i in range(1, numberToCheck+1):
		if numberToCheck % i == 0:
			print("Found a factor: " + str(i))
			print("Now, is it prime?")
	
if __name__ == "__main__":
	main()

