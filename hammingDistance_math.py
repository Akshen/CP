def optimalhamming(L):
    hammingdistance = 0
    for i in range(32):
        setbitCount = 0
        unsetbitCount = 0
        for j in range(len(L)):
            if(L[j] & 1<<i) > 0:
                setbitCount +=1
            else:
                unsetbitCount +=1
        hammingdistance += (2* setbitCount * unsetbitCount) % 10000007
        hammingdistance = hammingdistance % 10000007
    return hammingdistance

f = optimalhamming([2,4,6])
print(f)
