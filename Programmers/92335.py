def solution(n, k):
    answer = 0
    num = change(n, k)
    a = ''
    res = []
    for i in num:
        if i != 0:
            a += str(i)
        elif i == 0 and a:
            res.append(int(a))
            a = ''
    if a:
        res.append(int(a))
    
    for i in res:
        if is_Prime(i) == 1:
            answer += 1
    return answer

# 일반 범위 사용시, 1번 테케 런타임에러 
def is_Prime(n):
    if n < 2:
        return 0
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1

def change(n, k):
    res = []
    while n >= k:
        res.append(n%k)
        n = n // k 
    res.append(n)
    return res[::-1]

print(solution(437674, 3))
print(solution(110011, 10))
print(solution(36, 3))