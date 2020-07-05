#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    long int i,N, temp,count;
    vector <long int> vec;
    cin>>t;
    while(t--){
        count =0;
        cin>>N;
        vec.clear();
        for (i=0;i<N;i++){
            cin>>temp;
            vec.push_back(temp);
            
        }
        for (i=0;i<N-1;i++){
            count+=abs(vec[i+1]-vec[i])-1;
        }
        cout<<count<<endl;
    }
    return 0;
}