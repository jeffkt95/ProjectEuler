import sys
import os
import math

def isPrime(number):
	#Starting with the sqrt, factor1 is always a whole number.
	#If you find any whole number that multiplied times factor1 gives you
	#the argument number, then it's not prime.
	factor1 = math.floor(math.sqrt(number))
	while (factor1 > 1):
		factor2 = number / factor1
		if (factor2 % 1 == 0):
			#Found two whole numbers that give you number. It's not prime.
			#print("   " + str(number) + " is not prime because " + str(factor1) + " * " + str(factor2) + " = " + str(number))
			return False
		factor1 = factor1 - 1
	
	#print("   " + str(number) + " is prime.")
	return True

def main():
	primeCount = 0
	primeCountTarget = 10001
	i = 2
	
	while True:
		if (isPrime(i)):
			primeCount = primeCount + 1
			if (primeCount == primeCountTarget):
				print("Found prime number " + str(primeCountTarget) + ". It's " + str(i))
				return
			#else:
				#print("Found prime number " + str(primeCount) + ". It's " + str(i))
		i = i + 1
				
	
if __name__ == "__main__":
	main()

