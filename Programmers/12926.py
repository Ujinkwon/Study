def solution(s, n):
    answer = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in s:
        if i.isupper():
            i = i.lower()
            if alpha.index(i) + n > 25:
                answer += alpha[alpha.index(i) + n - 26].upper()
            else:
                answer += alpha[alpha.index(i) + n].upper()
        elif i.islower():
            if alpha.index(i) + n > 25:
                answer += alpha[alpha.index(i) + n - 26]
            else:
                answer += alpha[alpha.index(i) + n]
        else:
            answer += ' '
    return answer

print(solution('AB', 1))
print(solution('z', 1))
print(solution('a B z', 4))