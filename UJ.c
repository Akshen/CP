#include <stdio.h>
void quicksort(long arr[],long left, long right){
	long i = left,j = right;
	long temp, pivot = arr[(i+j)>>1];

	/* partition */
	while(i<=j){
		while(arr[i] <  pivot)
				i++;
		while(arr[j] > pivot)
				j--;
		if(i <= j){
			temp = arr[i];
			arr[i] = arr[j];
			arr[j] = temp;
			i++;
			j--;
		}

		if(left < j)
			quicksort(arr,left,j);

		if(i < right)
			quicksort(arr,i,right);
	}
	//return 0;
}

void binary_search(long arr, long size, long find){
	long low = 0, high = size;
	long mid = (low + high)>>1;
	long key = find;

	while(low <= high){
		if(key == mid){
			printf("%ld\n",mid );
			break;
		}

		if(key > mid){
			low = mid;
			mid = (low + high)>>1;
		}

		if(key < mid){
			high = mid;
			mid = (low + high)>>1;
		}
	}

}

long int fastInput() {
    long int val = 0;
    char c = getchar_unlocked();
    while (c < '0' || c > '9') c = getchar_unlocked();
    while (c >= '0' && c <= '9') {
        val = (val<<1) + (val<<3) + (c-'0');
        c = getchar_unlocked();
    }
    return val;
}

int main(){
	int t;
	unsigned long K,i,N;
	
	t = fastInput();
	while(t--){
		N = fastInput();
		unsigned long arr[N];
		for(i=0;i<N;i++){
			arr[i]=0;
		}
		

		for(i=0;i<N;i++){
			arr[i] = fastInput();
		}
		K = fastInput(); 
		K = arr[K-1];

		quicksort(arr,0,N);
		binary_search(arr,N,K);
		

	}
	return 0;
}