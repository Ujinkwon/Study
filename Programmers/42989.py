def solution(m, n, puddles):
    answer = 0
    q = [[0, 0, 0]]
    res = []
    while q:
        i, j, cnt = q.pop(0)
        if i == n-1 and j == m-1:
            res.append(cnt)
        for di, dj in [[0, 1], [1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < m and [nj+1, ni+1] not in puddles:
                q.append([ni, nj, cnt+1])
                
    answer = res.count(min(res)) % 1000000007
    return answer


print(solution(4, 3, [[2, 2]]))