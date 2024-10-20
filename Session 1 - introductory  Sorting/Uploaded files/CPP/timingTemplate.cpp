#include <cstdio>
#include <ctime>

using namespace std;

int main () {
    
	// Start measuring time
    clock_t startTime = clock();
    
    double sum = 0;
    for (int i=1; i<=1000000000; i++) {
        sum += i;
    }
    printf("Result: %.20f\n", sum);
	
    // Stop measuring time and calculate the elapsed time
    clock_t endTime = clock();
    double elapsed = double(endTime - startTime)/CLOCKS_PER_SEC;
    printf("Time measured: %.3f seconds.\n", elapsed);
    
    return 0;
}
