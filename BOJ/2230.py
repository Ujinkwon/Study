import sys
sys.stdin = open('2230.txt')

n, m = map(int, input().split())
# arr = [int(input())]
# min_value = 2000000000
# for _ in range(n-1):
#     num = int(input())
#     for i in range(len(arr)):
#         cal = abs(arr[i] - num)
#         if cal >= m and cal < min_value:
#             min_value = cal
#     arr.append(num)
# print(min_value)

arr = [int(input()) for _ in range(n)]
arr.sort()
left, right = 0, 1
res = 2000000000
while left < n and right < n:
    temp = arr[right] - arr[left]
    if temp == m:
        res = temp
        break
    elif temp > m:
        left += 1
        if res > temp:
            res = temp
    else:
        right += 1

print(res)