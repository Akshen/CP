from math import factorial
sum = 0
fact = 0
dp = []
n,k = map(long,raw_input().split())
l = (raw_input().split())

for i in xrange(len(l)):
	if long(l[i]) not in dp:
		dp[i+1]=factorial(long(l[i]))

	


print dp
print l
