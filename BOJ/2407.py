n, m = map(int, input().split())
p = f = 1
for i in range(n, n-m, -1):
    p *= i
for i in range(1, m+1):
    f *= i
print(p//f)