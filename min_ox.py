def minxor(B):
    B = sorted(B)
    ans = 999999999
    for i in range(len(B)-1):
        if ans > B[i] ^ B[i+1]:
            ans=B[i] ^ B[i+1]
    return ans