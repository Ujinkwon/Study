n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)

res = []
for i in range(len(arr)):
    res.append(arr[i]*(i+1))
print(max(res))