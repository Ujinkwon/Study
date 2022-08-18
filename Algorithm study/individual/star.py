
# 1
num = int(input())

for i in range(1, num+1):
    print(i*'*')


# 2
num = int(input())

for i in range(1, num+1):
    print(' '*(num-i) + '*'*i)


# 3
num = int(input())

for i in range(num, 0, -1):
    print('*'*i)


# 4
num = int(input())

for i in range(num, 0, -1):
    print(' '*(num-i) + '*'*i)


# 5
num = int(input())

for i in range(1, num+1):
    print(' '*(num-i) + '*' * (2 * i - 1) + ' '*(num-i))

# 6
num = int(input())

for i in range(num, 0, -1):
    print(' '*(num-i) + '*' * (2 * i - 1) + ' '*(num-i))

# 7
num = int(input())

