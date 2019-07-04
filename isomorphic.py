a,b=input().split(' ')
if(len(a)!=len(b)):
  print('no')
for i in a:
  c=a.count(i)
for i in b:
  d=b.count(i)
if((a==c)and(b==d)):
  print("yes")
else:
  print("no")
