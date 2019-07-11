a=input()
for i in range (0,len(a)):
    if(a[i].isupper()):
        print(a[i].lower(),end='')
    if(a[i].islower()):
        print(a[i].upper(),end='')

