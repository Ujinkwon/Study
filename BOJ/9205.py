import sys
sys.stdin = open('9205.txt')

def bfs():
    q = [[home[0], home[1]]]
    while q:
        x, y = q.pop(0)
        if abs(x - festival[0]) + abs(y - festival[1]) <= 1000:
            return 'happy'
        for i in range(n):
            if not visited[i]:
                nx, ny = store[i]
                if abs(x - nx) + abs(y - ny) <= 1000:
                    q.append([nx, ny])
                    visited[i] = 1
    return 'sad'

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    home = list(map(int, input().split()))
    store = [list(map(int, input().split())) for _ in range(n)]
    festival = list(map(int, input().split()))
    visited = [0 for _ in range(n+1)]
    print(bfs())