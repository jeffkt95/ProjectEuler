import sys
import os
import math

def main():
	sum = 0
	for i in range(1, 1000):
		if i % 3 == 0:
			sum = sum + i
			print("Found a multiple of 3: " + str(i))
		elif i % 5 == 0:
			sum = sum + i
			print("Found a multiple of 5: " + str(i))
	
	print sum
	
	
if __name__ == "__main__":
	main()

