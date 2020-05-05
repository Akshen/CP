string Solution::convert(string A, int B){
    if(A.empty()) {
        return "";
    }
    if (B==1){
        return A;
    }

    vector <string> ans(B);
    int n = A.size();
    int current_row = 0;
    int current_direction = 1;

    for(int i;i<n; ++i){
         ans[current_row] += A[i];
         if(current_row == 0){
             current_direction +=1;
         } else if(current_row == B -1) {
            current_direction = -1;
         }
         current_row += current_direction;
    }

    string final_str;
    for(auto row: ans){
            final_str +=row;
    }

    return final_str;



}