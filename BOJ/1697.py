def bfs():
    q = [n]
    while q:
        x = q.pop(0)
        if x == k:
            return distance[x]
        for i in (x-1, x+1, x*2):
            if 0 <= i <= max and not distance[i]:
                q.append(i)
                distance[i] = distance[x] + 1
    return -1

n, k = map(int, input().split())
max = 10 ** 5
distance = [0]*(max+1)
print(bfs())