import sys
sys.stdin = open('5431.txt')

t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    arr = list(range(1, n+1))
    print(f'#{tc}', *list(set(arr)-set(nums)))