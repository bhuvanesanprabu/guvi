a,b=map(int,(input()).split())
for i in range (2,10000):
    if(b%i==0 and a%i==0):
        m=i
print(m)
        
