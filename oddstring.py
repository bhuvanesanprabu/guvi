v=input()
j=list(v)
j[::2],j[1::2]=j[1::2],j[::2]
''.join(j)
print(*j,sep="")
