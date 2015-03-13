'''n=input()
while(n>0):
	a,b = map(int,raw_input().split())
	mul = a * b
	print mul
	n -=1

#Other Programs
t=input()
while(t>0):
	n,m=map(str,raw_input().split())
	N=n[::-1]
	M=m[::-1]
	a=int(N)
	b=int(M)
	sum = a + b
	ans=str(sum)
	SUM=ans[::-1]
	ANS=int(SUM)

	print ANS
	t -=1



N=[]
t=input()
while(t>0):
	n=a=b=1
	n,a,b = map(int,raw_input().split())
	
	for i in range(n):
		c=input()
		N.append(c)


	if(N[n-1]==b and N[0]==a):
		print ("BOTH")
	elif(N[0]==a and N[n-1]!=b):
		print ("EASY")
	elif(N[0]!=a and N[n-1]==b):
		print ("HARD")
	else:

		print ("OKAY")
	
	N=[]
	t -=1
'''
#Encrpytion

from string import maketrans
    
og="abcdefghijklmnopqrstuvwxyz0123456789"
Og="stuvwxyz0123456789abcdefghijklmnopqr"
print "A.Encrypt"
print "B.Decrypt"
     
n=raw_input()

if (n=="A"):
	N=raw_input()
	table=maketrans(og,Og)
	#for id in xrange(len(N)):
 	print N.translate(table) 
if (n=='B'):
	N=raw_input()
	table=maketrans(Og,og)
	#for i in xrange(len(N)):
	print N.translate(table)


