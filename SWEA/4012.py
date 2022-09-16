import sys
sys.stdin = open('4012.txt')
from itertools import combinations

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    idx = list(combinations(list(range(n)), n//2))
    a = []
    b = []
    res = []
    for i in range(len(idx)//2):
        a.append(idx[i])
        b.append(idx[len(idx)-1-i])
    for k in range(len(a)):
        acombi = list(combinations(list(a[k]), 2))
        bcombi = list(combinations(list(b[k]), 2))
        atotal = 0
        btotal = 0
        for l in range(len(acombi)):
            atotal += arr[acombi[l][0]][acombi[l][1]] + arr[acombi[l][1]][acombi[l][0]]
            btotal += arr[bcombi[l][0]][bcombi[l][1]] + arr[bcombi[l][1]][bcombi[l][0]]
        res.append(abs(atotal-btotal))
    print(f'#{tc} {min(res)}')