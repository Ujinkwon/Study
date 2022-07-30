def pibo(n):
    if n < 2:
        return n
    
    else:
        return pibo(n-1) + pibo(n-2)


n = int(input())
print(pibo(n))