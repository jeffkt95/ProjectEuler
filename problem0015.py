import sys
import os
import math
from numpy import *

def main():
	#This solution is based on the fact that the number of routes to any node
	#is the sum of the routes to the node above it, and the node to the left of it.
	#In other words, the number of routes to a particular node is the sum of the 
	#the routes from any nodes that could get you to that node.
	gridSize = 20
	
	numNodes = gridSize + 1
	numRoutes = 0
	
	numRoutesToNode = zeros((numNodes, numNodes))
	
	numRoutesToNode[0][0] = 1
	
	for row in range(0, numNodes):
		for col in range(0, numNodes):
			if (row > 0 and col > 0):
				numRoutesToNode[row][col] = numRoutesToNode[row-1][col] + numRoutesToNode[row][col-1]
			elif (row > 0):
				numRoutesToNode[row][col] = numRoutesToNode[row-1][col]
			elif (col > 0):
				numRoutesToNode[row][col] = numRoutesToNode[row][col-1]

	print("Grid of size " + str(gridSize) + " has " + str(numRoutesToNode[numNodes-1][numNodes-1]) + " routes.")
	
if __name__ == "__main__":
	from timeit import Timer
	t = Timer("main()", "from __main__ import main")
	print("Elapsed time for this problem: " + str(t.timeit(1)) + " seconds.")

