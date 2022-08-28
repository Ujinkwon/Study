import sys, itertools
sys.stdin = open('14889.txt')

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
total = []
perm = itertools.combinations(list(range(n)), n//2)
perm =  list(perm)

res = 10000
for i in range(len(perm)):
    ij = itertools.permutations(list(perm[i]), 2)
    ij = list(ij)
    cal = 0
    for j in range(len(ij)):
        cal += arr[ij[j][0]][ij[j][1]]
    total.append(cal)
for i in range(len(total)//2):
    gap = abs(total[i] - total[len(total)-1-i])
    if gap <= res:
        res = gap

print(res)