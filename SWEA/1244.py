import sys
from itertools import combinations
sys.stdin = open('1244.txt')

def change(n, arr):
    global max_value
    if n == int(cnt):
        if int(''.join(arr)) > max_value:
            max_value = int(''.join(arr))
        return
    for i in case:
        arr[i[0]], arr[i[1]] = arr[i[1]], arr[i[0]]
        num = ''.join(arr)
        # 교환 횟수마다 가능한 경우의 수에서 중복 거르기
        if num not in visited[n]:
            visited[n].append(num)
            change(n+1, arr)
        arr[i[0]], arr[i[1]] = arr[i[1]], arr[i[0]]

t = int(input())
for tc in range(1, t+1):
    nums, cnt = input().split()
    nums = list(nums)
    case = list(combinations(list(range(len(nums))), 2))
    visited = [[] for _ in range(10)]
    max_value = 0
    change(0, nums)
    print(f'#{tc} {max_value}')