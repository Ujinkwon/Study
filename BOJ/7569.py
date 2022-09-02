import sys
sys.stdin = open('7569.txt')

for _ in range(3):
    m, n, h = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(n)]