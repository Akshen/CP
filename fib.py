'''t=input()
count = 1
while(t>0):
	A= raw_input()
	a=len(A)
	for i in range(a):
		if(A[i]!=A[a-1]):
			if(A[i]==A[i+1]):
				count +=1

		else:
			print A[i],count
			count = 1
	t-=1
'''

'''

#Factorial Program!!
t = input()
while(t>0):
	count = 0
	fact = 1
	t -= 1
	a = input()
	for i in range(1,a):
		fact *= i

	A = str(fact)
	a = A[::-1]
	for i in range(len(a)):
		if (i==0):
			count +=1
		else:
			continue
	print count 
'''
#Brain Dump Prime Number
n=input()
print n
List=[]
i=I=0
while(n>0):
	i=n%2
	print i,n
	List.append(int(i))
	n=n/2
List=List[::-1]
print List
	

