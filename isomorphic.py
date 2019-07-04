a,b=input().split(' ')
if(len(a)!=len(b)):
  print('no')
for i in a:
  c=a.count(i)
for i in b:
  d=b.count(i)
if(c==d):
  print("yes")
else:
  print("no")
