import sys
sys.stdin = open('9205.txt')
def num(n):
    if n < 0:
        return -n
    else:
        return n

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    home = list(map(int, input().split()))
    store = [list(map(int, input().split())) for _ in range(n)]
    festival = list(map(int, input().split()))

    res = 'happy'

    for i in range(n):
        posx, posy = store[i][0], store[i][1]
        distance = abs(num(home[0]) - num(posx)) + abs(num(home[1]) - num(posy))
        if distance > 1000:
            d = abs(num(festival[0]) - num(home[0])) + abs(num(festival[1]) - num(home[1]))
            if d > 1000:
                res = 'sad'
            break
        home[0], home[1] = posx, posy
        
    else:
        distance = abs(num(festival[0]) - num(home[0])) + abs(num(festival[1]) - num(home[1]))
        if distance > 1000:
                res = 'sad'
    print(res)