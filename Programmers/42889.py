def solution(N, stages):
    answer = []
    cnt, human = [0] * max(stages), [len(stages)] * max(stages)
    ret = []
    total = 0
    for i in stages:
        cnt[i-1] += 1

    for i in range(N):
        human[i] = len(stages)-total
        total += cnt[i]
        ret.append(cnt[i] / human[i])

    for i in range(N):
        answer.append(ret.index(max(ret))+1)
        ret[ret.index(max(ret))] = -1
    return answer

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4,[4,4,4,4,4]))