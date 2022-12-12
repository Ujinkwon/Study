def find(x, par):
    if par[x] != x:
        par[x] = find(par[x], par)
    return par[x]

def union(a, b, par):
    root_a, root_b = find(a, par), find(b, par)
    if root_a <= root_b:
        par[b] = a
    else:
        par[a] = b

def solution(n, wires):
    par = [0] * (n+1)
    for i in range(n+1):
        par[i] = i
    
    arr = []
    for i in range(n):
        for j in range(n):
            if i != j and wires:
    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))