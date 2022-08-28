def solution(arr):
    answer = []
    arr.remove(min(arr))
    if len(arr) == 0:
        answer = [-1]
    else:
        answer = arr
    return answer

print(solution([4,3,2,1]))
print(solution([10]))