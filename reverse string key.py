a=int(input())
s=input()
a=(s.translate({ord(i):None for i in 'aeiou'}))
print(a[::-1])
