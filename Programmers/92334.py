def solution(id_list, report, k):
    answer = [0]*len(id_list)
    arr = dict()
    for i in id_list:
        arr[i] = 0
    mail = [[arr]]*len(id_list)

    for i in report:
        a, b = i.split()
        mail[id_list.index(a)][0][b] += 1
        print(mail)

    for i in range(len(mail)):
        for j in mail[i][0].values():
            if j >= k:
                answer[i] += 1
            
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
