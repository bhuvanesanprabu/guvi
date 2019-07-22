a=int(input())
p=a
q=[]
for i in range(p):
    s=list(map(int,input().split()))
    q+=s
q.sort()
print(*q)
