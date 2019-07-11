import collections

a=int(input())
c=[]
for i in range(0,a):
    b=input()
    c.append(b)

aa = collections.Counter(c).most_common(1)[0]
print(aa[0])

