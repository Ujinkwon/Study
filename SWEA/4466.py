import sys
sys.stdin = open('4466.txt')

t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    scores = list(map(int, input().split()))
    scores.sort(reverse=True)

    print(f'#{tc} {sum(scores[:k])}')