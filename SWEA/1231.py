import sys
sys.stdin = open('1231.txt')

def inorder(idx):
    res = ''
    if idx*2 < v+1:
        res += inorder(idx*2)
    res += arr[idx]
    if idx*2+1 < v+1:
        res += inorder(idx*2+1)
    return res

for tc in range(1, 11):
    v = int(input())
    arr = [0]*(v+1)
    for _ in range(v):
        a = list(input().split())
        arr[int(a[0])] = a[1]
    print(f'#{tc} {inorder(1)}')