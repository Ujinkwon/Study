def solution(N, stages):
    answer = []
    cnt, human = [0] * max(stages), [len(stages)] * max(stages)
    ret = []
    total = 0
    for i in stages:
        cnt[i-1] += 1
    for i in range(max(stages)):
        human[i] = len(stages)-total
        total += cnt[i]
        ret.append(cnt[i] / human[i])
    while len(ret) < N:
        ret.append(0)
    if len(ret) > N:
        ret = ret[:N]

    for i in range(N):
        answer.append(ret.index(max(ret))+1)
        ret[ret.index(max(ret))] = -1
    return answer

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4,[4,4,4,4,4]))
print(solution(5,[3,3,4]))