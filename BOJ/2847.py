n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
cnt = 0
for i in range(n-2, -1, -1):
    while arr[i+1] <= arr[i]:
        arr[i] -= 1
        cnt += 1
print(cnt)