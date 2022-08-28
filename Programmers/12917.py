def solution(s):
    answer = ''
    s = sorted(list(s), reverse=True)
    for i in s:
        answer += i
    return answer

print(solution('Zbcdefg'))