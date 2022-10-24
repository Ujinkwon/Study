from itertools import combinations

def solution(orders, course):
    answer = []
    res = dict()
    for i in orders:
        for k in course:
            if len(i) < k:
                break
            arr = list(combinations(i, k))
            for j in arr:
                j = ''.join(sorted(j))
                if j not in res.keys():
                    res[j] = 1
                else:
                    res[j] += 1
    max_value = [1] * len(course)
    arr = [[] for _ in range(len(course))]
    for i in res.items():
        for j in range(len(course)):
            if len(i[0]) == course[j]:
                if max_value[j] < i[1]:
                    max_value[j] = i[1]
                    arr[j] = [i[0]]
                elif max_value[j] > 1 and max_value[j] == i[1]:
                    arr[j].append(i[0])
    for i in arr:
        for j in i:
            answer.append(j)
    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))