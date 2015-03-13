from sys import stdin
def main():
  l=[]
  for t in xrange(input()):
    n,q=map(int,stdin.readline().split())
    l=range(n)
    a=map(int,stdin.readline().split())
    for __ in xrange(q):
        A=map(int,stdin.readline().split())
        B=range(A[0]-1,A[1])
        C=list(set(l)-set(B))
        result=a[C[0]]
        for i in C:
           w=gcd(result,a[i])
        print w


def gcd(a,b):
  while b:
    a,b = b, a% b 
  return a

if __name__ == '__main__':
  main()