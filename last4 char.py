a,v=input().split(' ')
b=int(v)
c=[]
for i in range(1,b+1):
    c.append(a[-i])
c.reverse()
print(''.join(c))
