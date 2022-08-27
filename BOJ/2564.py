import sys
sys.stdin = open('2564.txt')

r, c = map(int, input().split())
n = int(input())
store = [list(map(int, input().split())) for _ in range(n)]
d, x = map(int, input().split())
total = 0

