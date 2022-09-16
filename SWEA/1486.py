import sys
sys.stdin = open('1486.txt')
from itertools import combinations

t = int(input())
for tc in range(1, t+1):
    n, b = map(int, input().split())
    h = list(map(int, input().split()))
    min_value = 10001
    total = []
    for i in range(len(h)+1):
        for j in list(combinations(h, i)):
            if sum(list(j)) >= b:
                total.append(sum(list(j)) - b)
    print(f'#{tc} {min(total)}')