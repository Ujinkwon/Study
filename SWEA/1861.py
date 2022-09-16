import sys
sys.stdin = open('1861.txt')

def bfs(i, j, n):
    q = [(i, j)]
    cnt = 1
    while q:
        i, j = q.pop(0)
        for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < n and room[ni][nj]-1 == room[i][j]:
                    q.append((ni, nj))
                    cnt += 1
    return cnt
                    

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    room = [list(map(int, input().split())) for _ in range(n)]
    arr = []
    idx = []
    for i in range(n):
        for j in range(n):
            res = bfs(i, j, n)
            idx.append([j, i])
            arr.append(res)
    min_room = 1000000
    for i in range(len(arr)):
        if max(arr) == arr[i] and room[idx[i][1]][idx[i][0]] < min_room:
            min_room = room[idx[i][1]][idx[i][0]]
            
    print(f'#{tc} {min_room} {max(arr)}')