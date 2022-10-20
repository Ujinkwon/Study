from itertools import permutations

def nums(n, s):   # n 개수, s 합
    if n > s:
        return -1
    p, q = divmod(s, n)
    ret = [p]*n
    for i in range(q):
        ret[i] += 1
    return sorted(ret)


def solution(n, info):
    answer = []
    for i in range(1,n+1):
        arr = nums(i, n)
        for j in range(11-len(arr)):
            arr.append(0)
        case = list(set(permutations(arr)))
        print(case)
    #     max_vlaue = 0
    #     res = []
    #     for j in case:
    #         lion_total = 0
    #         apeach_total = 0
    #         for k in range(11):
    #             lion = list(j)
    #             if lion[k] > info[k]:
    #                 lion_total += (10 - k)
    #             if lion[k] <= info[k] and not (lion[k] == info[k] == 0):
    #                 apeach_total += (10 - k)
    #         if lion_total - apeach_total > max_vlaue:
    #             max_vlaue = lion_total - apeach_total
    #             res.append(lion_total - apeach_total)
    #     print(res)
    return answer


print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
# print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
# print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
# print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))