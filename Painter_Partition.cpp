const long int mod = 10000003;

bool paintCheck(int num_ofPainter, long int time_per_unit, vector<int> &fence_len, long int time_per_painter){
    int painter_used = 1;
    long int c_time_used = 0;
    
    for(auto length: fence_len){
        if(length * time_per_unit > time_per_painter){
            return false;
        }
        
        c_time_used += length * time_per_unit;
        if(c_time_used > time_per_painter){
            ++painter_used;
            c_time_used = length*time_per_unit;
        }
    }
    
    return painter_used <= num_ofPainter;
    
}

int Solution::paint(int A, int B, vector<int> &C) {
    unsigned long int l = 1;
    unsigned long int r = 0;
    
    for(auto length: C){
        r +=length;
    }
    r *=B;
    unsigned long int ans = -1;
    
    while(l <=r){
        unsigned long int mid = l + (r - l)/2;
        
        if(paintCheck(A, B, C, mid)){
            ans = mid;
            r = mid - 1;
        } else {
            l = mid + 1;
        }
    }
    
    return ans%mod;
}

