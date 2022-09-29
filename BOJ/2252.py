import sys
from collections import deque
sys.stdin = open('2252.txt')

n, m = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)   # 작은키 => 큰키 라고 했을 때 출발하는 곳을 인덱스로 하고 보내는 곳을 값으로
    indegree[b] += 1  # indegree 개수 담은 배열

q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:  # indegree가 0인 정점들 q에 추가
        q.append(i)

while q:
    num = q.popleft()   # pop해서 출력하고
    print(num, end=' ')
    for i in arr[num]:   # 뽑은 정점에서 도착하는 곳들 indegree -1
        indegree[i] -= 1
        if indegree[i] == 0:  # indegree 0으로 변경되면 q에 추가
            q.append(i)