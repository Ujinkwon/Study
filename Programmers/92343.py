def dfs(node, nodes, zero, one, visited):
    global max_cnt, adj, wolfcheck
    # nodes += adj[node]
    nodes = list(set(nodes+adj[node]))

    if zero <= one or not nodes:
        return
    for i in nodes:
        if not visited[i]:
            visited[i] = 1
            if wolfcheck[i]:
                dfs(i, nodes, zero, one+1, visited)
            else:
                dfs(i, nodes, zero+1, one, visited)
            visited[i] = 0
    max_cnt = max(max_cnt, zero)

def solution(info, edges):
    global max_cnt, adj, wolfcheck
    wolfcheck = info
    n = len(info)
    adj = [[] for _ in range(n)]
    visited = [0 for _ in range(n)]
    visited[0] = 1
    max_cnt = 1
    for p, c in edges:
        adj[p].append(c)
    dfs(0, [0], 1, 0, visited)
    return max_cnt


print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
print(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))