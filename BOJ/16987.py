import sys
sys.stdin = open('16987.txt')

t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for i in range(n):
        s, w = map(int, input().split())
        arr.append([s,w])