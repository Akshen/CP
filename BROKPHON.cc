//CodeChef:BROKPHON
#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long int ull;
int main()
{
	int test;
	ull i,N,sum;
	ull v[1000001];
	scanf("%d",&test);
	while(test--)
	{
		scanf("%llu",&N);
		fill(v,v+1000001,0);sum=0;
		for(i=1;i<=N;i++)
		{
			scanf("%llu",&v[i]); 
			
		}
		for(i=1;i<=N;i++){
			if(i==1){
				if(v[i]!=v[i+1]){
					sum++;
						
				}
			}
			else{
				if(i!=N && v[i]!=v[i+1]){
					sum++;
				
					
				}
				else{
					if(v[i]!=v[i-1]){
						sum++;
						
					}
				}
			}
		}
		printf("%llu\n",sum);
	}
	return 0;
}