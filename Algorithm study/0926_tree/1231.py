import sys
sys.stdin = open('1231.txt')

def inorder(n):
    if n:
        inorder(ch1[n])
        print(par[n], end='')
        inorder(ch2[n])

for _ in range(10):
    v = int(input())
    ch1 = [0]*(v+1)
    ch2 = [0]*(v+1)
    par = [0]*(v+1)
    for i in range(1, v+1):
        arr = list(input().split())
        for j in range(2, len(arr)):
            if ch1[int(arr[0])] == 0:
                ch1[int(arr[0])] = int(arr[j])
            else:
                ch2[int(arr[0])] = int(arr[j])
        par[int(arr[0])] = arr[1]
    inorder(1)
    print()
