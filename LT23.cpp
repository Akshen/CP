#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	long len;
	char L1,L2,V[1000001];
	scanf("%d",&t);
	while(t--){
			bool flag = 0;
			fill(V,V+1000001,0);
			scanf("%s",V);
			L1 = V[0];	L2=V[1]; len = strlen(V);
			if(L2==L1){
				flag = 1;
				goto ans;
			}
			for(long i=0;i<len;){
				if(i!=len-1){			
					if(L1==V[i] && L2==V[i+1]){
						i+=2;
					}
					else{
						flag = 1;
						break;
					}
				}
				else{
					if(i%2==0){
						if(L1!=V[i])
						{
							flag = 1;
							break;
						}
						else{
							i++;
						}
					}
					else{
						if(L2!=V[i]){
							flag = 1;
							break;
						}
						else{
							i++;
						}
					}
				}

			}
			
			ans : (flag)?printf("NO\n"):printf("YES\n");
	}
	return 0;
}