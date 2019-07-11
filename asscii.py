a=input()
b=''
c='0ABCDEFGHIJKLMNOPQRSTUVWXYZABC'
for i in a:
    if i in c:
        d=c.index(i)
        d=d+3
        b=b+c[d]
print(b)
