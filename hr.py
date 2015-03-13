#Hacker rank Contest
'''n=input()
D=map(int,raw_input().split())
d = {x:D.count(x) for x in D}
a,b = d.keys(),d.values()
l = len(b)
b.sort()
if(all(x == D[0] for x in D)):
	print D[0]
elif(b[l-1]==b[l-2]):
	print -1
else:
	print max(d.keys(),key=lambda x: d[x])
	
#Dinosour and Villagers Codechef Competition.
import sys
for __ in range(input()) :
	n=input()
	feed,ind=0,0
	lists=list(map(int,sys.stdin.readline().split()))
	for i in range(n) :
		ind+=lists[i]
		print ind
		if ind > 0 :
			feed+=ind
		else :
			feed-=ind
	print feed
'''


i = set(raw_input())
print str(i)