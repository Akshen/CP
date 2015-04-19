/*author:Akshen Doke
Codechef:VCS
*/
#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef long int l;
int main()
{
int test;
l C,c,i,M,K,N;
scanf("%d",&test);
while(test--){
scanf("%ld%ld%ld",&N,&M,&K);
l arr[N+1];
    fill(arr,arr+N+1,0);
    C = M+K;
    for(i=1;i<=C;i++){

    scanf("%ld",&c);
    arr[c]++;

    }

    C = 0;c = 0;

    for(i=1;i<=N;i++){

        if(arr[i]==2){
            c+=1;

        }
        else if(arr[i]==0){
            C+=1;
        }
    }

   printf("%ld %ld\n",c,C);


}

return 0;
}
