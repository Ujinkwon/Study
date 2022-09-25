import sys
sys.stdin = open('3.txt')

def inorder(s):
    global num
    if s <= n:
        inorder(2*s)
        tree[s] = num
        num += 1
        inorder(2*s+1)

t = int(input())
for _ in range(t):
    n = int(input())
    tree = [0]*(n+1)
    num = 1
    inorder(1)
    print(tree[1], tree[n//2])