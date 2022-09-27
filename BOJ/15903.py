import sys
sys.stdin = open('15903.txt')

# for tc in range(2):
#     n, m = map(int, input().split())
#     arr = list(map(int, input().split()))
#     for _ in range(m):
#         min1 = min(arr)
#         arr.remove(min1)
#         min2 = min(arr)
#         arr.remove(min2)
#         arr += [min1+min2, min1+min2]
#     print(f'#{tc} {sum(arr)}')

n, m = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(m):
    min1 = min(arr)
    arr.remove(min1)
    min2 = min(arr)
    arr.remove(min2)
    arr += [min1+min2, min1+min2]
print(sum(arr))