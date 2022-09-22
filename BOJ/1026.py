import sys
sys.stdin = open('1026.txt')

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
total = 0
for _ in range(n):
    total += max(b)*min(a)
    b.remove(max(b))
    a.remove(min(a))
print(total)