import sys
import os
import math

def traceRoute(row, col, maxRow, maxCol, numRoutes):
	if (row == maxRow and col == maxCol):
		numRoutes = numRoutes + 1
		return numRoutes
	if (row < maxRow):
		numRoutes = traceRoute(row + 1, col, maxRow, maxCol, numRoutes)
	if (col < maxCol):
		numRoutes = traceRoute(row, col + 1, maxRow, maxCol, numRoutes)
		
	return numRoutes

def main():
	gridSize = 13
	numRoutes = 0
	
	numRoutes = traceRoute(0, 0, gridSize, gridSize, numRoutes)
	print("Grid of size " + str(gridSize) + " has " + str(numRoutes) + " routes.")
	
if __name__ == "__main__":
	from timeit import Timer
	t = Timer("main()", "from __main__ import main")
	print("Elapsed time for this problem: " + str(t.timeit(1)) + " seconds.")

