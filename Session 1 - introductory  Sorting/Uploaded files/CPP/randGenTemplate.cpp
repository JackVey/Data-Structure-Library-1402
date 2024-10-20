#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int *randArray(int seed, int n){
  int *A = new int[n];
  srand(seed);
  for(int i=0;i<n;i++)
    A[i]=rand();
  return A;
}

int main(void) {
  int n = 100;
	int *A = randArray(1401, n);
    for (int i = 0; i < n; i++) {
      cout<<A[i]<<" ";
    }
	return 0;
}
