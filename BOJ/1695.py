def bfs(n):
    q = [[n, 1]]
    while q:
        n, cnt = q.pop(0)
        for dn in [n*2, n*10+1]:
            if dn == b:
                return cnt+1
            elif dn <= b:
                q.append([dn, cnt+1])
    return -1

a, b = map(int, input().split())
print(bfs(a))