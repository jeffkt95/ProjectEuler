import sys
import os
import math

def isPrime(number):
	if (number == 1):
		return False
	elif (number < 4):  #2 and 3 are prime
		return True
	elif (number % 2 == 0):   #all evens except 2 are not prime
		return False
	elif (number < 9):   #4, 6, and 8 are covered
		return True
	elif (number % 3 == 0):
		return False

	#See solution to problem 7
	upperBound = math.floor(math.sqrt(number))
	possibleFactor = 5
	while (possibleFactor <= upperBound):
		if (number % possibleFactor == 0):
			return False
		elif (number % (possibleFactor + 2) == 0):
			return False
		possibleFactor = possibleFactor + 6
		
	#print(str(number) + " is prime!!!")
	return True

def main():
	sum = 0
	upperBound = 2e6
	#upperBound = 20   #correct answer: 77
	#upperBound = 30   #correct answer: 129
	#upperBound = 40   #correct answer: 197
	#upperBound = 50   #correct answer: 
	#upperBound = 60   #correct answer: 
	#upperBound = 70   #correct answer: 568
	i = 2
	while i < upperBound:
		if (isPrime(i)):
			sum = sum + i
			#print(str(i) + " is prime!! New sum is " + str(sum))
		if (i % 100000 == 0):
			print("On " + str(i) + ". Going to " + str(upperBound))
		i = i + 1
	
	print("The sum of all primes below " + str(upperBound) + " is " + str(sum))

	
if __name__ == "__main__":
	from timeit import Timer
	t = Timer("main()", "from __main__ import main")
	print t.timeit(1)
	#main()
