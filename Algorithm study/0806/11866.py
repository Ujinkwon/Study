n, k = map(int, input().split())

stack = []
list = list(range(1, n+1))
idx = k-1

while list:
    stack.append(list.pop(idx))
    if list:
        idx = ((idx-1) + k) % len(list)
    
print('<', end='')
for i in range(len(stack)):
    if i == len(stack)-1:
        print(stack[i], end='')
    else:
        print(stack[i], end=', ')
print('>')