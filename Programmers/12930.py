def solution(s):
    word = list(s.split(" "))             # split() VS split(" ")
    new_word = []
    for i in word:
        answer = ''
        for j in range(len(i)):
            if j % 2:
                answer += (i[j].lower())
            else:
                answer += (i[j].upper())
        new_word.append(answer)
    return ' '.join(new_word)

print(solution("try hello world"))
print(solution("tr y h e l l o w o r ld "))
print(solution(" T Ry HeLLO WOrld "))