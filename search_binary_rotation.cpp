#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	

	int small_index = -1;
	int N = A.size();
	int l = 0; int r  = N - 1;
	
	while(l<=r){
		int mid = l + (r - l)/2;
		
		if(A[mid]>A[N - 1]){
			l = mid +1 ;
		} else {
			small_index = mid;
			r = mid - 1;
		}
	}
	l = 0; r = N - 1;
	while (l <= r){
		int mid = l + (r - l)/2;
		int new_index = (mid + small_index)%N;

		if(A[new_index] < X){
			l = mid + 1;

		} else if (A[new_index] > X){
			r = mid - 1;
		} else {
			return new_index;
		}
	}
	return -1;
}