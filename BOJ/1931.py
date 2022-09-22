import sys
sys.stdin = open('1931.txt')

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x:(x[1], x[0]))
cnt = 1
print(arr)

a = arr[0][1]
for i in range(1, len(arr)):
    if a <= arr[i][0]:
        a = arr[i][1]
        cnt += 1

print(cnt)