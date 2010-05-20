import sys
import os
import math

def isPalindrome(number):
	numAsString = str(number)
	numAsStringReversed = numAsString[::-1]
	
	return numAsString == numAsStringReversed

def main():
	numForCheck = 21012
	largestPalindrome = -1
	
	for i in range(1, 1000):
		for j in range(1, 1000):
			product = i * j
			ispalindrome = isPalindrome(product)
			if(ispalindrome and product > largestPalindrome):
				largestPalindrome = product
		
	print("The largest palindrome is: " + str(largestPalindrome))
	
if __name__ == "__main__":
	main()

