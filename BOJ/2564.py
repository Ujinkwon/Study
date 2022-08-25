import sys
sys.stdin = open('2564.txt')

r, c = map(int, input().split())
n = int(input())
store = [list(map(int, input().split())) for _ in range(n)]
human = map(int, input().split())

# 1 4
# 3 2
# 2 8
# 2 3

# 4-3 = 1
# [0] 다르면 + c
# + 3*2 
# 12

# 8-3 = 5
# 5
