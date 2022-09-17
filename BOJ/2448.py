n = int(input())

def basic(a):
    if a == 1:
        res = '*'
    elif a == 2:
        res = '* *'
    elif a == 0:
        res = '*'*5
    return res

for i in range(1, n+1):
    print(' '*(n-i) + basic(i%3))
