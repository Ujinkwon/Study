import sys
sys.stdin = open('5688.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    num = round(n**(1/3))
    if num**3 == n:
        res = num
    else:
        res = -1
    print(f'#{tc} {res}')