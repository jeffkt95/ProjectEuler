#include <iostream>
#include <time.h>

typedef unsigned int uint;

uint nextStep(uint row, uint col, uint maxRow, uint maxCol, uint numRoutes) {
   if (row == maxRow && col == maxCol) {
      numRoutes++;
      return numRoutes;
   }
   if (row < maxRow) {
      numRoutes = nextStep(row + 1, col, maxRow, maxCol, numRoutes);
   }
   if (col < maxCol) {
      numRoutes = nextStep(row, col + 1, maxRow, maxCol, numRoutes);
   }
   return numRoutes;
}

void problem15() {
   uint numRoutes = 0;
   uint maxCol = 20;
   uint maxRow = 20;

   numRoutes = nextStep(0, 0, maxRow, maxCol, numRoutes);

   std::cout << "The number of routes for " << maxRow << "x" << maxCol << " grid is "
      << numRoutes << std::endl;
}

void main() {
   clock_t start,end;

   start = clock();
   problem15();
   end = clock();

   double diffInSeconds = (double)(double)(end - start) / (double)CLOCKS_PER_SEC;

   std::cout << diffInSeconds << " seconds to solve this problem." << std::endl;
}