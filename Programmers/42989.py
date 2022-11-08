def solution(m, n, puddles):
    answer = 0
    q = [[0, 0, 0]]
    res = []
    min_cnt = m*n
    while q:
        i, j, cnt = q.pop(0)
        if min_cnt < cnt:
            continue
        if i == n-1 and j == m-1:
            if min_cnt == cnt:
                res.append(cnt)
            elif min_cnt > cnt:
                res = [cnt]    
                min_cnt = cnt
        else:
            for di, dj in [[0, 1], [1, 0]]:
                ni, nj = i+di, j+dj
                if 0 <= ni < n and 0 <= nj < m and [nj+1, ni+1] not in puddles:
                    q.append([ni, nj, cnt+1])

    cnt = len(res)
    if cnt >= 1000000007:
        answer = cnt % 1000000007
    else:
        answer = cnt
    return answer


print(solution(4, 3, [[2, 2]]))