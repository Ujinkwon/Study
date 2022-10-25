# def solution(info, query):
#     answer = []
#     for i in query:
#         temp = list(i.replace('and ', '').split())
#         cnt = 0
#         for j in info:
#             arr = list(j.split())
#             for k in range(4):
#                 if temp[k] == '-':
#                     continue
#                 if temp[k] != arr[k]:
#                     break
#             else:
#                 if int(temp[4]) <= int(arr[4]):
#                     cnt += 1
#         answer.append(cnt)
#     return answer

from itertools import  combinations

def solution(info, query):
    answer = []
    dic = dict()
    score = []
    arr = [[] for _ in range(len(info))]
    for i in info:
        temp = list(i.split())
        if temp[-1] not in score:
            score.append(temp[-1])
        for k in range(1, 5):
            arr[score.index(temp[-1])].append(list(combinations(temp[:4], k)))
    for i in arr:
        print(i)
    print(score)
    return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))