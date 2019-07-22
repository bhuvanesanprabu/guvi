f=int(input())
c=0
for i in range(0,f):
  if(pow(2,i)>f):
    break
  c=f-pow(2,i)
print(c)
