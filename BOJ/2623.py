import sys
sys.stdin = open('2623.txt')

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
for _ in range(m):
    temp = list(map(int, input().split()))
    for i in range(1, temp[0]):
        arr[temp[i]].append(temp[i+1])
        indegree[temp[i+1]] += 1
q = []
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)
res = []
while 1:
    if q == []:
        break
    num = q.pop(0)
    res.append(num)
    for i in arr[num]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)
    if not q and len(res) != n:
        res = [0]
        break
for i in res:
    print(i)