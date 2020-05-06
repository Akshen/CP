def revbit(B):
    left = 32
    right = -1
    while(left>right):
        left -=1
        right +=1
        isSetLeft = (B>>left)&1
        isSetRight = (B>>right)&1
        if isSetLeft ^ isSetRight:
            B ^= (1 << left)
            B ^= (1 << right)
    return B