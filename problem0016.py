import sys
import os
import math
from numpy import *

def main():
	answer = math.pow(2, 1010)
	print(str(answer))

if __name__ == "__main__":
	from timeit import Timer
	t = Timer("main()", "from __main__ import main")
	print("Elapsed time for this problem: " + str(t.timeit(1)) + " seconds.")

