import sys
sys.stdin = open('1541.txt')

# 마이너스 기준으로 괄호치면 최소값! => 최대한 큰 값을 빼야되니까
arr = list(input())
a = ''
res = []
for i in range(len(arr)):
    if arr[i] != '-':
        a += arr[i]

    if arr[i] == '-' or i == len(arr)-1:
        if '+' in a:
            nums = list(map(int, a.split('+')))
            res.append(sum(nums))
        else:
            res.append(int(a))
        a = ''
total = res[0]
for i in range(1, len(res)):
    total -= res[i]
print(total)