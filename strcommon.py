a,b=input().split(' ')
c=0
for i in range(0,len(a)):
    if(a[i]==b[i]):
        c=c+1
if(len(a)==(c+1)):
    print("yes")
else:
    print("no")


