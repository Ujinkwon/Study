a, b, c = map(int, input().split())

if a == b == c:
    money = 10000 + (a*1000)
elif a == b:
    money = 1000 + (a*100)
elif a == c:
    money = 1000 + (a*100)
elif b == c:
    money = 1000 + (b*100)
else:
    if a > b :
        if c > a:
            money = c*100
        else: 
            money = a*100

    elif a < b:
        if c > b:
            money = c*100
        else: 
            money = b*100

print(money)