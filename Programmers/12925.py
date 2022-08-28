def solution(s):
    answer = 0
    if s[0] == '-':
        num = int(s[1:])
        answer = -num
    elif s[0] == '+':
        answer = int(s[1:])
    else:
        answer = int(s)
    return answer

print(solution('1234'))
print(solution('-1234'))