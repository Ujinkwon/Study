def solution(left, right):
    answer = 0
    arr = []
    for k in range(left, right+1):
        cnt = 0
        for i in range(1, k+1):
            if k % i == 0:
                cnt += 1
        arr.append(cnt)
    for i in range(len(arr)):
        if arr[i] % 2:
            answer -= (left + i)
        else:
            answer += (left + i)
    return answer

print(solution(13,17))
print(solution(24,27))