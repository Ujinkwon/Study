def cal_power(a, b, c):
    result = 1
    while b:
        if b % 2 == 1:
            result = result * a % c
        a = a * a % c
        b //= 2
    return result

a, b, c = map(int, input().split())
print(cal_power(a, b, c))