def solution(answers):
    answer = []
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt = [0, 0, 0]
    for i in range(len(answers)):
        if (i+1) % 5 == answers[i] % 5:
            cnt[0] += 1

        if b[i % 8] == answers[i]:
            cnt[1] += 1

        if c[i % 10] == answers[i]: 
            cnt[2] += 1

    for k in range(len(cnt)):
        if max(cnt) == cnt[k]:
            answer.append(k+1)

    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))