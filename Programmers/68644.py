def solution(numbers):
    arr = []
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            arr.append(numbers[i] + numbers[j])
    arr = list(set(arr))
    arr = sorted(arr)
    return arr


print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))