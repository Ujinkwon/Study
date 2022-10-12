import sys
from itertools import permutations
sys.stdin = open('1767.txt')

def dfs():
    # if cnt == len(core):
    #     if total < min_value:
    #         min_value = total
    # elif total >= min_value:
    #     return

    # else:
        for di, dj in [[0,1], [0,-1], [1,0], [-1,0]]:
            visited_temp = visited[:]
            ni, nj = i+di, j+dj
            cnt, flag = 0, 0
            while 0 <= ni < n and 0 <= nj < n:
                if not visited_temp[ni][nj] and not arr[ni][nj]:
                    visited_temp[ni][nj] = 1
                    ni += di
                    nj += dj
                    cnt += 1
                else:
                    flag = 1
                    break
            if not flag: 
                if cnt < min_cnt:
                    min_cnt = cnt
                    temp = visited_temp

        total += min_cnt
        visited = temp[:]

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    core = []
    for i in range(1, n-1):
        for j in range(1, n-1):
            if arr[i][j]:
                core.append([i, j])
    case = list(permutations(list(range(1, len(core)+1)), len(core)))
    visited = [[0]*n for _ in range(n+1)]
    min_cnt = 13

    print(f'#{tc}')