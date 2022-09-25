import sys
from itertools import combinations
sys.stdin = open('2115.txt')

def ff(array):
    res = 0
    for i in range(1, len(array)+1):
        arr = list(combinations(array, i))
        for j in arr:
            total = 0
            for k in j:
                total += k*k
            if sum(j) <= c and total > res:
                res = total
    return res

t = int(input())
for tc in range(1, t+1):
    n, m, c = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    a_list = [[] for _ in range(n)]
    b_list = [[] for _ in range(n)]
    max_value = 0
    for i in range(n):
        for j in range(n-m+1):
            for l in range(i+1, n):
                a = ff(arr[i][j:j + m])
                for q in range(n-m+1):
                    b = ff(arr[l][q:q+m])
                    if a + b > max_value:
                        max_value = a+b
    print(f'#{tc} {max_value}')