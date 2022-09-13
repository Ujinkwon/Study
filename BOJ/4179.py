import sys
sys.stdin = open('4179.txt')

r, c = map(int, input().split())
maze = [(input().split()) for _ in range(c)]

print(maze)