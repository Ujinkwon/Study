def solution(nums):
    answer = 0
    cal = []
    for i in range(len(nums) - 2):
        for j in range(1, len(nums) - 1):
            for k in range(2, len(nums)):
                if i != j != k and i < j < k:
                    cal.append(nums[i] + nums[j] + nums[k]) 
    
    for m in cal:
        for n in range(2, m):
            if m % n == 0:
                break
        else:
            answer += 1
            
    return answer

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))