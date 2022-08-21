import sys
sys.stdin = open('2527.txt')

for _ in range(4):
    lx1, ly1, rx1, ry1, lx2, ly2, rx2, ry2 = map(int, input().split())
    if rx1 