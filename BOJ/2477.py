k = int(input())
xmax, ymax = 0, 0
stack = []
for i in range(6):
    d, n = map(int, input().split())
    if d == 1 or d == 2:
        if xmax < n:
            xmax = n
    elif d == 3 or d == 4:
        if ymax < n:
            ymax = n
    stack.append(n)
stack.index(xmax)
stack.index(ymax)


print(stack)
print(k * ((xmax*ymax)))
