from sys import stdin
def main():
	n = input()
	while n:
		Li = []
		N,K = map(int,stdin.readline().split())
		l = (map(int,stdin.readline().split()))
		Li= l[::-1]
		while K:
			L,R = map(int,stdin.readline().split())
			if L==R:
				del l[L-1]
				if len(l)==1:
					print l[0]
				else:
					p = gcd(l[0],l[len(l)-1])
					print p
			else:
				L -=1
				R -=1
				index = L,R
				l=[i for j,i in enumerate(l) if j not in index]

				if len(l)==1:
					print l[0]
				else:
					p = gcd(l[0],l[len(l)-1])
					print p

			l = Li[::-1]
			K-=1
		n -=1

def gcd(a,b):
	while b:
		a,b=b,a%b
	return a

if __name__ == '__main__':
	main()