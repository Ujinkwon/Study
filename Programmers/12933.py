def solution(n):
    answer = ''
    arr = []
    for i in str(n):
        arr.append(int(i))
    arr = sorted(arr, reverse=True)
    for i in arr:
        answer += str(i)
    return int(answer)

print(solution(118372))