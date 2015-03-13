t = input()
while t:
	n = raw_input()
	if len(n)>0:
		n =int(n)
		Li = []
		while n:
			Li.append((raw_input())
			n-=1
		Li.sort()
		d= {d:Li.count(d) for d in Li}
		#sorted(d)
		a,b = d.values(),d.keys()
		b.sort()
		for i in range(len(a)):
			print b[i],a[i]
		t -=1