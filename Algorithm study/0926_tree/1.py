def find_root(v):
    for i in range(1, v+1):
        if par[i] == 0:
            return i

def preorder(n):
    if n:
        print(n, end=' ')
        preorder(ch1[n])
        preorder(ch2[n])

v = int(input())
arr = list(map(int, input().split()))
ch1 = [0]*(v+1)
ch2 = [0]*(v+1)
par = [0]*(v+1)
for i in range(0, len(arr), 2):
    p, c = arr[i], arr[i+1]
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c
    par[c] = p
root = find_root(v)
preorder(root)
print()