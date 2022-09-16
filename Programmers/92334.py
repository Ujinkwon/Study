def solution(id_list, report, k):
    
    n = len(id_list)
    arr = [[0]*n for _ in range(n)]
    for i in range(len(report)):
        a, b = report[i].split()
        arr[id_list.index(a)][id_list.index(b)] = 1
    total = [0]*n
    answer = [0]*n
    for i in range(n):
        for j in range(n):
            total[j] += arr[i][j]
    for l in range(len(total)):
        if total[l] >= k:
            for i in range(n):
                if arr[i][l] == 1:
                    answer[i] += 1

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
