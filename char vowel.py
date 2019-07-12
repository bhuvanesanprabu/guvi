a=input()
b='aeiou'
c=0
v=0
for i in a:
    if(i in b):
        print("Vowel")
        c=c+1
        break
if(c==0):
    for i in a:
        if(i.isalpha()):
                print("Consonant")
                v=v+1
                break
if(c==0 and v==0):
    print("invalid")
                
