from itertools import combinations
from itertools import combinations

def nums(n, s):
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
        print(nums(i, n))
    return answer


print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))