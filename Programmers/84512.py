def solution(word):
    alpa = {'A':'E', 'E':'I', 'I':'O', 'O':'U'}
    now = 'A'
    cnt = 1
    while word != now:
        cnt += 1
        if len(now) < 5:
            now += 'A'
        elif len(now) == 5:
            now = list(now)
            temp = now.pop()
            while temp == 'U':
                temp = now.pop()
            now.append(alpa[temp])
            now = ''.join(now)
    return cnt

print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))