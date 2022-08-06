n, k = int(input().split())

stack = []
list = list(range(1, n+1))

while list:
    stack = list.pop(k)
