import sys
sys.stdin = open('1959.txt')

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if len(a) > len(b):
        big = a
        small = b
    else:
        big = b
        small = a

    max_total = 0
    for i in range(abs(len(a) - len(b))+1):
        total = 0
        for j in range(len(small)):
            total += small[j] * big[i+j]
            
        if max_total < total:
            max_total = total
    
    print(f'#{tc} {max_total}')