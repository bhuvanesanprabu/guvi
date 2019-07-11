a,b=map(int,(input()).split())
for i in range (2,10000):
    if(i%b==0 and i%a==0):
        print(i)
        break
