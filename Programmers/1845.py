def solution(nums):
    answer = 0
    stack = []
    for i in nums:
        if i not in stack:
            stack.append(i)
    if len(nums) // 2 < len(stack):
        answer = len(nums) // 2
    else:
        answer = len(stack)
        
    return answer

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))