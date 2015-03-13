from collections import OrderedDict
t = input()
while t > 0:
	D = raw_input()
	'''d = {x:D.count(x) for x in D}

	a ,b= sorted(d.keys())'''
	d = OrderedDict(sorted(D.items(),key=itemgetter()))
	b = d.values()
	c =len(b)
	print a,b
	if(c ==1 or b[c-1]>b[c-2] ):
		print 'YES'
	else:
		print 'NO'
	t -=1