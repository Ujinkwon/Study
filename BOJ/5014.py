import sys
sys.stdin = open('5014.txt')

def bfs():
    q = [s]
    visited[s] = 1
    while q:
        x = q.pop(0)
        if x == g:
            return cnt[g]
        for i in (x+u, x-d):
            if 0 < i <= f and not visited[i]:
                q.append(i)
                cnt[i] = cnt[x] + 1
                visited[i] = 1
    if cnt[g] == 0:
        return "use the stairs"

f, s, g, u, d = map(int, input().split())
cnt = [0]*(f+1)
visited = [0]*(f+1)
print(bfs())