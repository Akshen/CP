from __future__ import division

#Series Solution
from sys import stdin
t=int(stdin.readline())
while t>0:
	gs=raw_input().split()
	a=int(gs[0])
	b=int(gs[1])
	c=int(gs[2])
	flag = total = dif= 0
	pos = int(stdin.readline())
	if ((b/a) == (c/b) or a==b==c):
		print "YES"
		diff=b/a
		flag = 1
		total = a+b+c
	elif(b-a == c-b):
		print "YES"
		diff=c-b	
		flag = 2
		total = a+b+c
	else:
		print "NO"
		flag = 0
	if(flag == 1):
		ans = c
		if(pos <=len(gs)):
			print gs[pos-1]
			print int(total)
		elif(diff==1 and a!=b):
			for i in range(len(gs),pos):
				ans +=diff
				total +=ans
			print int(ans)
			print int(total)
		elif(diff==1 and a==b==c):
			for i in range(len(gs),pos):
				total +=ans
			print int(ans)
			print total
		else:	
			for i in range(len(gs),pos):
				ans *=diff
				total +=ans
			print int(ans)
			print int(total)
	elif(flag==2):
		ans = c
		if(pos<=len(gs)):
			print gs[pos-1]
			print total
		else:
			for i in range(len(gs),pos):
				ans +=diff
				total+=ans
			print ans
			print total
	t -=1


	