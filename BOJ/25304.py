total = int(input())
cnt = int(input())
total2 = 0
for _ in range(cnt):
    money, cnt2 = map(int, input().split())
    total2 += money * cnt2

if total == total2:
    print('Yes')

else:
    print('No')