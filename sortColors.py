def SolutionColors(SC):
    n = len(SC)
    s= 0
    e = n -1
    i = 0
    while i<=e:
        if SC[i] == 0:
            SC[i], SC[s] = SC[s], SC[i]
            s+=1
        elif SC[i] == 2:
            SC[i], SC[e] = SC[e], SC[i]
            e -=1
            continue
        i+=1
    return SC

print(SolutionColors([0,1,0,2,1,1,1]))