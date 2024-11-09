template <typename T> void BlockSwap(T *A,int p, int q) {
	// TO DO
}

template <typename T> int StableRBA(T *A,int p,int q,int r) {
	int n0 = r-q;
	int n1= q-p;
	if( n1==0 ) return r;
	while(n0>0) {
		if( n1>n0) {
			p=q-n0;
			BlockSwap(A,p,q);
			n1=n1-n0;
			q=p;
			p=p-n1;
		}
		else {
			BlockSwap(A,p,q);
			n0=n0-n1;
			p=q;
			q=q+n1;
		}
	}
	return p;
}

template <typename T> int BinaryStableSort(T *A,int p,int r) {
	if(r-p>1) {
		int q= (p+r)/2;
		p=BinaryStableSort(A,p,q);
		r=BinaryStableSort(A,q,r);
		p=StableRBA(A,p,q,r);
	}
	else if(!A[p].key()) // return ?;
	return p;
}


#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;

class aclass{
	int k;
	char satellite;
public:
    aclass(){}
	aclass(int key, char data){
		k=key;
		satellite=data;
	}
	bool key(){ return k; }
	void print(){
		cout<<" ("<<k<<","<<satellite<<")";
	}
};

int main(int argc, char *argv[]) {
	aclass A[26];
	int i;
	for(i=0;i<26;i++) {
		A[i]=aclass(rand()%2,i+97);
	}
	
	for(i=0;i<26;i++) A[i].print();
	 cout<<endl;
	 
	 BinaryStableSort(A,0,26);
	 
	for(i=0;i<26;i++) A[i].print();
	 cout<<endl;
}