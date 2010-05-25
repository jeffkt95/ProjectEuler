import sys
import os
import math

def nextStep(row, col, maxRow, maxCol, numRoutes):
	if (row == maxRow and col == maxCol):
		numRoutes = numRoutes + 1
		return numRoutes
	if (row < maxRow):
		numRoutes = nextStep(row + 1, col, maxRow, maxCol, numRoutes)
	if (col < maxCol):
		numRoutes = nextStep(row, col + 1, maxRow, maxCol, numRoutes)
	return numRoutes

def main():
	numRoutes = 0
	maxRow = 2
	maxCol = 2
	
	for i in range(0, maxRow):
		for j in range(1, maxCol):
	
	numRoutes = nextStep(0, 0, 15, 15, numRoutes)
	
	print("The number of routes is " + str(numRoutes))
	
if __name__ == "__main__":
	from timeit import Timer
	t = Timer("main()", "from __main__ import main")
	print("Elapsed time for this problem: " + str(t.timeit(1)) + " seconds.")

