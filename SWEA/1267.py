import sys, copy
sys.stdin = open('1267.txt')

for tc in range(1, 5):
    v, e = map(int, input().split())
    arr = list(map(int, input().split()))
    node = [[] for _ in range(v+1)]
    for i in range(e):
        print(arr[i*2], arr[i*2+1])
        node[arr[i*2]].append(arr[i*2+1])
    print(node)
    print(f'#{tc}')