import sys
sys.stdin = open('1932.txt')

# def dfs(i, c, total):
#     global max_value
#     if c == n:
#         if total > max_value:
#             max_value = total
#     else:
#         for di in [i, i+1]:
#             if 0 <= di < n:
#                 dfs(di, c+1, total+arr[c][di])

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# max_value = 0
# dfs(0, 1, arr[0][0])
# print(max_value)

for i in range(1, n):
    for j in range(len(arr[i])):
        if j == 0:
            arr[i][j] += arr[i-1][j]
        elif j == len(arr[i])-1:
            arr[i][j] += arr[i-1][j-1]
        else:
            arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])
print(max(arr[n-1]))