import sys
sys.stdin = open('5648.txt')

def ff(array):
    pos = []
    for i in array:
        if i[2] == 0:  # 상
            i[1] += 1
        elif i[2] == 1:
            i[1] -= 1
        elif i[2] == 2:
            i[0] -= 1
        else:
            i[0] += 1


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(ff(arr))

    print(f'#{tc}')