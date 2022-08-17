n = int(input())

cnt = 0
l = []
while n != 1:
    l.append(n)
    if n % 3 == 0:
        n = n // 3
    elif (n-1) % 3 == 0:
        n = n-1 // 3
        cnt += 1
    elif n % 2 == 0:
        n = n // 2
    elif (n-1) % 2 == 0:
        n = n-1 // 2
        cnt += 1
    else:
        n -= 1
    cnt += 1
l.append(1)
print(cnt)
print(*l)