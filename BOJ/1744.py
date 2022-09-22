def cal(arr):
    global total
    if len(arr) % 2:
        end = len(arr)-1
        total += arr[-1]
    else:
        end = len(arr)
    for i in range(0, end, 2):
        total += arr[i] * arr[i+1]

n = int(input())
plus = []
minus = []
total = 0
for _ in range(n):
    num = int(input())
    if num > 1:
        plus.append(num)
    elif num == 1:
        total += 1
    else:
        minus.append(num)
plus.sort(reverse=True)
minus.sort()
cal(plus)
cal(minus)
print(total)

# 0, 양수 => 덧셈
# 0, 음수 => 곱셈
# 1, x => 덧셈
# 양수, 양수 => 곱셈
# 양수, 음수 => 덧셈
# 음수, 음수 => 곱셈

# 음수+0 : 오름차순
# 양수 : 내림차순
# 1은 더하기
# 각 리스트 두개씩 곱해서 더하기