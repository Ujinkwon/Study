import sys
sys.stdin = open('4008.txt')

def dfs(total, idx):
    global min_value, max_value
    if idx == n:
        if total > max_value:
            max_value = total
        if total < min_value:
            min_value = total
        return
    for i in range(4):
        if operator[i]:
            if i == 0:
                operator[i] -= 1
                dfs(total+nums[idx], idx+1)
                operator[i] += 1
            elif i == 1:
                operator[i] -= 1
                dfs(total-nums[idx], idx+1)
                operator[i] += 1
            elif i == 2:
                operator[i] -= 1
                dfs(total*nums[idx], idx+1)
                operator[i] += 1
            elif i == 3:
                operator[i] -= 1
                dfs(int(total/nums[idx]), idx+1)
                operator[i] += 1

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    operator = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    min_value, max_value = 10**8, -10**8
    dfs(nums[0], 1)
    print(f'#{tc} {max_value-min_value}')