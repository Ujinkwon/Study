n = int(input())

if n % 2:
    for i in range(1, 2*n+2):
        if i % 3 == 1:
            print('*'*(2*i-1))
        