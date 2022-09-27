import sys
sys.stdin = open('1865.txt')

def ff(idx, s):
    global max_value

    if idx == n:
        if s > max_value:
            max_value = s
    elif s <= max_value:
        return
    else:
        for i in range(n):
            if not visited[i]:
                visited[i] = 1
                temp = s*p[idx][i]/100
                ff(idx+1, temp)
                visited[i] = 0

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    p = [list(map(int, input().split())) for _ in range(n)]
    max_value = 0
    visited = [0]*n
    ff(0, 1)
    print(f'#{tc}', '%.6f'%(max_value*100))
