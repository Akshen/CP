int Solution::singleNumber(const vector<int> &A){
    int ans = 0;
    for(int b = 0; b<32;b++){
        int countSetBit = 0;
        for(auto num: A){
            if((num >>b)& 1){
                countSetBit+=1;
            }
        }

        if(countSetBit % 3 != 0){
            ans |= (1 <<b);
        }

    }

    return ans;
}