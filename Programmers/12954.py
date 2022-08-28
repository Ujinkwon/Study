def solution(x, n):
    answer = []
    if x == 0:
        answer = [0]*n
    else:
        if x <= 0:
            end = x*n-1
        else:
            end = x*n+1
        for i in range(x, end, x):
            answer.append(i)
    return answer

print(solution(2,5))
print(solution(4,3))
print(solution(-4,2))
print(solution(0,3))