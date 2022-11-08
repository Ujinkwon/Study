def solution(info, query):
    answer = []
    for i in query:
        temp = list(i.replace('and ', '').split())
        cnt = 0
        for j in info:
            arr = list(j.split())
            for k in range(4):
                if temp[k] == '-':
                    continue
                if temp[k] != arr[k]:
                    break
            else:
                if int(temp[4]) <= int(arr[4]):
                    cnt += 1
        answer.append(cnt)
    return answer

# from itertools import  combinations

# def solution(info, query):
#     answer = [0]*len(info)
#     arr = []
#     for i in query:
#         temp = tuple(i.replace('and ', '').replace('-', '').split())
#         arr.append(temp)

#     for i in range(len(arr)):
#         score = int(arr[i][-1])
#         a = arr[i][:len(arr[i])-1]
#         for j in info:
#             temp = list(j.split())
#             for k in list(combinations(temp, len(arr[i]))):
#                 if k[-1].isdigit() and int(k[-1]) >= score and k[:len(k)-1] == a:
#                     answer[i] += 1
#     return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))