#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;


int mask;
bool radixkey(const int& x){ return x&mask; }

void inplaceRadixSort(int *x, int n){
	 mask=1;
	 while(mask){
	 	BinaryStableSort(x,0,n,radixkey);	 	
	 	mask<<=1;
	 }
}

int main(int argc, char *argv[]) {
	// TEST 
}