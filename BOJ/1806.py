import sys
sys.stdin = open('1806.txt')

n, s = map(int, input().split())
nums = list(map(int, input().split()))
left, right = 0, 0
total = nums[0]
res = 100000001
while 1:
    # 크거나 같으면 젤 왼쪽 값 빼주고 인덱스도 다음으로 이동 & 대소비교
    if total >= s:
        total -= nums[left]
        if res > (right - left + 1):
            res = right-left + 1
        left += 1
    # 작으면 오른쪽 한칸 이동후 값 추가 & 범위 체크
    else:
        right += 1
        if right == n:
            break
        total += nums[right]

if res == 100000001:
    res = 0
print(res)