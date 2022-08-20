student = int(input())
nums = list(map(int, input().split()))
line = [1] * student

for i in range(1, student):
    for j in range(nums[i]):
        line[i - j] = line[i-1 - j]
    line[i-nums[i]] = i+1
print(*line)