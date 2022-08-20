n, k = map(int, input().split())
room = [[0, 0] for _ in range(6)]
result = 0

for _ in range(n):
    s, y = map(int, input().split())
    room[y-1][s] += 1
    if room[y-1][s] == k:
        result += 1
        room[y-1][s] = 0
for i in room:
    for j in range(2):
        if i[j] != 0:
            result += 1
print(result)