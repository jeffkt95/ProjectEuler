import sys
import os
import math

def getNumDivisors(number):
	if (number == 1):
		return 1
		
	#All numbers except for 1 have at least two divisors: 1 and itself.
	divisorCount = 2
	
	#Starting with the sqrt, factor1 is always a whole number.
	factor1 = math.floor(math.sqrt(number))
	while (factor1 > 1):
		factor2 = number / factor1
		if (factor2 % 1 == 0):
			#Found two whole numbers that give you number. It's not prime.
			#print("   " + str(number) + " is not prime because " + str(factor1) + " * " + str(factor2) + " = " + str(number))
			divisorCount = divisorCount + 2
		factor1 = factor1 - 1

	return divisorCount

def main():
	maxIterations = 100000
	triangleNumber = 0
	
	for i in range(1, maxIterations + 1):
		triangleNumber = triangleNumber + i
		numDivisors = getNumDivisors(triangleNumber)
		if (numDivisors > 500):
			print("Triangle number " + str(i) + " is " + str(triangleNumber) + ". It has " + str(getNumDivisors(triangleNumber)) + " divisors.")
			return
		if (i== maxIterations):
			print("Got to max iteration and couldn't find it.")
			print("Triangle number " + str(i) + " is " + str(triangleNumber) + ". It has " + str(getNumDivisors(triangleNumber)) + " divisors.")
			
if __name__ == "__main__":
	from timeit import Timer
	t = Timer("main()", "from __main__ import main")
	print("Elapsed time for this problem: " + str(t.timeit(1)) + " seconds.")

