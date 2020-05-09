vector<int> Solution::prevSmaller(vector<int> &A) {
    int n = A.size();
    vector<int> ans(n, -1);
    
    stack <int> stk;
    
    for(int i = n-1; i>=0;i--){
        if(stk.empty() or A[stk.top()] <= A[i]){
            stk.push(i);
            continue;
        }
        while(!stk.empty() and A[stk.top()]> A[i]){
            ans[stk.top()] = A[i];
            stk.pop();
        }
        
        stk.push(i);
    }
    
    return ans;
}
