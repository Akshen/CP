def fact(n):
	f = n
	while (n>=1):
		f = f * (n-1)
		n = n - 1
	return f

def F(x):
	T = x*fact(x)
	return T

N,M = map(int,raw_input().split())
S = list(raw_input().split())

I = 0
L = len(S)

while (I<L):
	