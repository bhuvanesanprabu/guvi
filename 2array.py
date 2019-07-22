import math
a,b=map(int,input().split())
n1=a
n2=b
a=[]
l=list(map(int,input().split()))
for i in range(0,n2):
        a1,b1=map(int,input().split())
        a.append([a1,b1])
for i in a:
        x=i[0]-1
        y=i[1]-1
        print(math.gcd(l[x],l[y]))
