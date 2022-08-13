n = int(input())
family = [0] * n

a, b = map(int, input().split())
m = int(input())

for i in range(m):
    x, y = map(int, input().split())
    family[y-1] = x

cnt = 0

while family[a-1] != family[b-1]:
    
    cnt += 1
    
    if family[a-1] == 0:
        cnt = -2
        break

    a = family[a-1]

print(cnt + 1)