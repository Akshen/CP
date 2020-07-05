#include <bits/stdc++.h>
using namespace std;

int main(){
    unsigned short t, N, chef_scr, morty_scr;
    long int A_temp,B_temp, A,B,A_sum,B_sum;
    cin>>t;
    while (t--)
    {
        cin>>N;
        chef_scr = 0;
        morty_scr = 0;
        while(N--){
            A_sum = 0;
            B_sum = 0;
            cin>>A>>B;
            while(A){
                A_temp = A%10;
                A_sum+=A_temp;
                A/=10;
            }
            while(B){
                B_temp = B%10;
                B_sum+=B_temp;
                B/=10;
            }
            if(A_sum > B_sum){
                chef_scr +=1;
            } else if(A_sum == B_sum){
                chef_scr+=1; morty_scr+=1;
            }
            else {
                morty_scr +=1;
            }
        }
        if (chef_scr > morty_scr){
            cout<<0<<'\t'<<chef_scr<<endl;
        } else if(chef_scr == morty_scr){
            cout<<2<<'\t'<<chef_scr<<endl;
        } else {
            cout<<1<<'\t'<<morty_scr<<endl;
        }
    }
    

    return 0;
}