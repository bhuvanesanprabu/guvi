a=int(input())
for j in range(2,a+1):
  if(a%j==0):
      b=0
      for m in range(2,j+1):
          if(j%m==0) and (m!=j):
              b=1
              break
      if(b==0):
          print(j,end=' ')
