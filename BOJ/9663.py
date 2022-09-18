def dfs(x):
    global cnt
    if x == n:
        cnt += 1
    else:
        for i in range(n): 
            arr[x] = i
            for j in range(x):
                if arr[x] == arr[j] or abs(arr[x] - arr[j]) == x - j:
                    break
            else:
                dfs(x+1) 

# n = int(input())
n = 8
arr = [0] * n
cnt = 0
dfs(0)
print(cnt)