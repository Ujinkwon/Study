import sys
from itertools import combinations
sys.stdin = open('6603.txt')

def dfs(s, depth):
    if depth == 6:
        print(*combi)
        return
    for i in range(s, len(n)):
        combi[depth] = n[i]
        dfs(i+1, depth+1)

while 1:
    n = list(map(int, input().split()))
    if n[0] == 0:
        break
    del n[0]
    combi = [0]*6
    dfs(0,0)
    print()

# while 1:
#     n = list(map(int, input().split()))
#     if n[0] == 0:
#         break
#     nums = n[1:]
#     arr = combinations(nums, 6)
#     for i in arr:
#         print(*i)
#     print()

