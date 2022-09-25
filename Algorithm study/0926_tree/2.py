import sys
sys.stdin = open('2.txt')

def inorder(n):
    global cnt
    if n:
        inorder(ch1[n])
        cnt += 1
        inorder(ch2[n])

t = int(input())
for _ in range(t):
    e, n = map(int, input().split())
    arr = list(map(int, input().split()))
    ch1 = [0]*(e+2)
    ch2 = [0]*(e+2)
    for i in range(0, len(arr), 2):
        p, c = arr[i], arr[i+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c
    cnt = 0
    inorder(n)
    print(cnt)
