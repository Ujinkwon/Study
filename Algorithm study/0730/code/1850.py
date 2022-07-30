a, b = map(int, input().split())

# 유클리드 호제법
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

print('1'*gcd(a, b))



# import math
# a, b = map(int, input().split())
# print('1'*math.gcd(a, b))