def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]

    def dfs(tar):
        visited[tar] = 1
        for j in range(len(computers)):
            if j != tar and computers[tar][j] and not visited[j]:
                dfs(j)

    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]	))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]	))