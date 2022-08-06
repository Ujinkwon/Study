n = int(input())

for i in range(n):
    stack = []
    a = input()

    for k in a:
        if k == '(':
            stack.append(k)
        elif k == ')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break

    else:   # break안 걸렸을 때
        if not stack:
            print('YES')
        else:
            print('NO')