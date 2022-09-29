import sys
sys.stdin = open('1795.txt')

def dijstra(q, arr):
    while 1:
        min_value = 101
        for i in q:
            if i[0] not in U and i[1] < min_value:
                min_value = i[1]
                idx = i[0]
        total = min_value
        if idx == x:
            break
        U.append(idx)
        for i in range(len(arr[idx])):
            arr[idx][i][1] = min(arr[idx][i][1]+total, D[arr[idx][i][0]])
        q += arr[idx]
    print(total)

t = int(input())
for tc in range(1, t+1):
    n, m, x = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        s, e, w = map(int, input().split())
        adj[s].append([e, w])
    for k in range(1, n+1):
        if k != x:
            D = [0] + [10 ** 12] * n
            U = [k]
            for i in adj[k]:
                D[i[0]] = i[1]
            q = [*adj[k]]
            print(U, D, q)
            arr = adj[:]
            print(adj)
            dijstra(q, arr)

    print(f'#{tc}')