m=int(input())
a=input().split()
c=[]
for i in a:
    c.append(i)
c.sort(key=len)

for i in c:
    print(i,end=' ')

