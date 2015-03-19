// Rose Problem CodeChef Competition
#include <bits/stdc++.h>
int main () {
  int T,N;
   
   scanf("%d",&T);
   while(T--){
  scanf("%d",&N);
  long long D,S=0, I,L;
  while(N--)
      {
		
        scanf("%lld",&D);
        scanf("%lld",&L);
        I=L;
        while(I>0)
        {

          S+=I;
          I-=D;
         
        }
        
      }
      (S%2==0)?printf("NO\n"):printf("YES\n");
	}
  return 0;
}