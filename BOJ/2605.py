student = int(input())
nums = list(map(int, input().split()))
line = [0] * student

for i in range(len(nums)):
    for j in range(i):
        line[j+1] = line[j]
        print(line)