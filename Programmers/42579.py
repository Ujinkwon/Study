def solution(genres, plays):
    answer = []
    res = dict()
    for i in range(len(genres)):
        if genres[i] not in res.keys():
            res[genres[i]] = [plays[i]]
        else:
            res[genres[i]][0] += plays[i]
        res[genres[i]].append(plays[i])
    v = sorted(list(res.values()), reverse=True)
    for i in v:
        arr = i[1:]
        answer.append(plays.index(max(arr)))
        plays[plays.index(max(arr))] = -1
        arr.remove(max(arr))
        if arr:
            answer.append(plays.index(max(arr)))
    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print(solution(["classic", "pop", "classic", "classic"], [500, 600, 150, 800]))
print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 600]))