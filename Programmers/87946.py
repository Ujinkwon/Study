from itertools import permutations

def solution(k, dungeons):
    max_cnt = -1
    n = len(dungeons)
    temp = permutations(list(range(n)), n)
    for i in temp:
        # print(i)
        now = k
        cnt = 0
        for j in i:
            if now >= dungeons[j][0]:
                now -= dungeons[j][1]
                cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt
    return max_cnt

print(solution(80, [[80,20],[50,40],[30,10]]))