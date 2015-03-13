t = input()
while t:
	og = []
	S,B = map(int,raw_input().split())
	li= raw_input().split()
	for i in range(len(li)):
	og.append(int(li[i]))
	m = max(og)
	c = 0
	for i in range(B):
		if(c!=m):
			c +=og[i]
		else:
			og[i]=0
			c = 0
	if(og[S-1]==0):
		print "yes" 
	else:
 		print "no"
	t -=1
