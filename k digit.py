def red( a, b) :
    if b <= 0 : return n

    if a == 0 : return 10	# Fail
    p1 = red(a//10, b)*10 + n%10
    p2 = red(a//10, b-1)
    if p1 < p2 :
        return p1
    else :
        return p2


n, k = input().split()
n, k = int(n), int(k)
print(red(n, k)
