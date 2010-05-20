import sys
import os
import math

def main():
	for b in range(999, 1, -1):
		for a in range(b-1, 0, -1):
			result = 1e6 - 2000 * a - 2000 * b + 2 * a * b
			if (result == 0):
				c = 1000 - a - b
				if (c > b):
					print("Found the answer! a is " + str(a) + " b is " + str(b))
					print("   c is " + str(c))
					print("Their sum is " + str(a + b + c))
					print("a^2 + b^2 is " + str(a * a + b * b))
					print("c^2 is " + str(c * c))
					print("   Their product is " + str(a * b * c))
					return
	
	print("Solution not found")
	
if __name__ == "__main__":
	main()
