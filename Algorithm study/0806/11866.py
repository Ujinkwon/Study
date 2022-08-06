n, k = map(int, input().split())

stack = []
list = list(range(1, n+1))
print(list)

while list:
    stack.append(list.pop(k))
    print(stack)