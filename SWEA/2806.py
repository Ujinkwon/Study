import sys
sys.stdin = open('2806.txt')

def dfs(x):
    global cnt
    if x == n:
        cnt += 1
    else:
        for i in range(n):
            arr[x] = i
            for i in range(x):
                if arr[x] == arr[i] or abs(arr[x] - arr[i]) == x - i:
                    break
            else:
                dfs(x+1)
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [0] * n
    cnt = 0
    dfs(0)
    print(f'#{tc} {cnt}')