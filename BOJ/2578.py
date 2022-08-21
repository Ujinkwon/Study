from audioop import bias
import sys
sys.stdin = open('2578.txt')

bing_go = [list(map(int, input().split())) for _ in range(5)]
nums = []
for i in range(5):
    n = input().split()
    for j in range(5):
        nums.append(int(n[j]))

result1, result2 = [], []
cnt = 0

for k in nums:
    for i in range(5):
        for j in range(5):
            if k == bing_go[i][j]:
                bing_go[i][j] = 0
                cnt += 1
            
    cnt3, cnt4 = 0, 0
    result = 0
    for i in range(5):
        cnt1, cnt2 = 0, 0
        for j in range(5):
            if bing_go[i][j] == 0:
                cnt1 += 1
                if cnt1 == 5 and [i, j] not in result1:
                    result1.append([i, j])

            if bing_go[j][i] == 0:
                cnt2 += 1
                if cnt2 == 5 and [j, i] not in result2:
                    result2.append([j, i])
        if bing_go[i][i] == 0:
            cnt3 += 1
            if cnt3 == 5:
                result += 1
        if bing_go[i][4-i] == 0:
            cnt4 += 1
            if cnt4 == 5:
                result += 1
    if result + len(result1) + len(result2) == 3:
        break

print(cnt)
