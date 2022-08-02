n, m = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()
solve = []

def Dfs(depth):
    if depth == m:
        print(' '.join(map(str, solve)))
        return

    for i in range(n):
        if depth

