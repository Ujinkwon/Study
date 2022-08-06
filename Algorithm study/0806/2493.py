n = int(input())

list = list(map(int, input().split()))

stack = []
a = [0 for _ in range(n)]

for i in range(len(list)-1, -1, -1):
    if len(stack) == 0:
        stack.append([i, list[i]])

    else:
        while list[i] > stack[len(stack)-1][1]:
            tower = stack.pop()
            a[tower[0]] = i+1

            if len(stack) == 0:
                break

        stack.append([i, list[i]])

for k in a:
    print(k, end=" ")