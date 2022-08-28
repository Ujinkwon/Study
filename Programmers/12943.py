def solution(num):
    answer = 0
    if num == 1:
        answer = 0
    else:
        while num != 1:
            if num % 2:
                num = num*3 + 1
            else:
                num = num // 2
            answer += 1
            if answer >= 500:
                answer = -1
                break
    return answer

print(solution(6))
print(solution(16))
print(solution(626331))
print(solution(1))