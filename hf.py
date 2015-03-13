t = input()
while t > 0:
	N,K = map(int,raw_input().split())
	'''ans = []
  	N,K = map(int,raw_input().split())
  	l = raw_input().split()
  	sorted(l)
  	for i in range(K):
  		ans += [[]]
  	print ans
'''
	li = []
	c = 0
	l = raw_input().split()
	for i in range(len(l)):
		for j in range(len(l)):
			c = int(l[i]) ^ int(l[j]) ^ K
			li.append(c)

	print max(li)
  	t -=1


    
    