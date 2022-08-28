def solution(n):
    answer = 0
    arr = ''
    while n > 2:
        arr += str(n % 3)
        n = n // 3
    arr += str(n)
    
    for i in range(len(arr)):
        num = int(arr[i])
        answer += num * (3 ** (len(arr)-1-i))
    
    return answer

print(solution(45))
print(solution(125))