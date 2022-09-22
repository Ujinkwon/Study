import sys
sys.stdin = open('2105.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    kind = [list(map(int, input().split())) for _ in range(n)]
    

    print(f'#{tc}')