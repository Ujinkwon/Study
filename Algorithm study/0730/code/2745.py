n, b = input().split()

n = ''.join(reversed(n))    # 뒤집어서 반복하는 게 편리
b = int(b)

number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # 36진법에 해당하는 문자열
result = 0

for i in range(len(n)-1, -1, -1):
    result += number.index(n[i]) * (b**i)
    # 해당 문자열에 해당하는 인덱스 값을 구함(동일), 진수에 i를 제곱(해당 자리위치 값)
print(result)