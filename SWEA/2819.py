import sys
sys.stdin = open('2819.txt')

def dfs(i, j, res):
    global ans
    if len(res) == 7:
        if res not in ans:
            ans.append(res)
        return
    for di, dj in [[0,1],[1,0],[-1,0],[0,-1]]:
        if 0 <= i+di < 4 and 0 <= j+dj < 4:
            dfs(i+di, j+dj, res+str(arr[i+di][j+dj]))

t = int(input())
for tc in range(1, t+1):
    arr = [list(input().split()) for _ in range(4)]
    ans = []
    for i in range(4):
        for j in range(4):
            dfs(i, j, arr[i][j])
    print(f'#{tc} {len(ans)}')