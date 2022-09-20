import sys
sys.stdin = open('2819.txt')
from itertools import combinations

arr = []
for i in range(4):
    for j in range(4):
        arr.append([i, j])
print(list(combinations(arr, 6)))

t = int(input())
for tc in range(1, t+1):
    table = [list(map(int, input().split())) for _ in range(4)]


    print(f'#{tc}')