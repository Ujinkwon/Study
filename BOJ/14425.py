import sys
sys.stdin = open('14425.txt')


n, m = map(int, input().split())
arr = [sys.stdin.readline() for _ in range(n)]
cnt = 0
for _ in range(m):
    text = sys.stdin.readline()
    if text in arr:
        cnt += 1
print(cnt)