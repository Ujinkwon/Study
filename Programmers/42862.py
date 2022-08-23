
def solution(n, lost, reserve):
    answer = 0
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            lost.remove(i)
    for i in lost:
        if i+1 in reserve:
            reserve.remove(i+1)
            answer += 1
        elif i-1 in reserve:
            reserve.remove(i-1)
            answer += 1
    answer += (n - len(lost))
    return answer

print(solution(5, [2,4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
print(solution(5, [1, 3], [1]))