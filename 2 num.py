a,b=list(map(int,input().split()))
ab=a
ab1=b
cb1=list(map(int,input().split()))
cb=[]
while(ab1):
    m = list(map(int,input().split()))
    cb.append(m)
    ab1-=1
for j in cb:
    va=0
    for k in range(j[0]-1,j[1]):
        va=va^cb1[k]
    print(va)
