from re import I


a, b, c = map(int, input().split())


revenu, total, cnt = 0, a, 0
while True:
    cnt += 1
    revenu += c
    total += b 

    if revenu > total:
        print(cnt)
        break

