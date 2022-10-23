import sys
sys.stdin = open('11660.txt')

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    total = 0
    for i in range(x1-1, x2):
        total += sum(arr[i][y1-1:y2])
    print(total)