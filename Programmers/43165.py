def dfs(idx, total):
    global nums, tar
    if idx == len(nums)-1:  # numbers 다 계산
        if total == tar:
            return 1
        else:
            return 0
    idx += 1   # numbers 순서대로 계산하기 위한 인덱스
    return dfs(idx, total+nums[idx]) + dfs(idx, total-nums[idx])

def solution(numbers, target):
    global nums, tar
    nums, tar = numbers, target
    return dfs(0, numbers[0]) + dfs(0, -numbers[0])

print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))