def isPrime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input())
num_list = list(map(int, input().split()))
cnt = 0


for i in range(n):
    if isPrime(num_list[i]) == True:
        cnt += 1

print(cnt)