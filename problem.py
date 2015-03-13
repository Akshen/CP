from math import factorial
tc = input()
while tc!=0:
	tc -=1
	n,k = map(int,raw_input().split())
	n = factorial(n)
	l = map(int,raw_input().split())
	print n%max(l)
