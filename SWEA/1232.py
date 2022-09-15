import sys
sys.stdin = open('1232.txt')

def postorder(n):
    global res
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        res.append(arr[n])

for tc in range(1, 11):
    n = int(input())
    arr = [0]*(n+1)
    ch1 = [0]*(n+1)
    ch2 = [0]*(n+1)
    for _ in range(n):
        a = list(input().split())
        arr[int(a[0])] = a[1]
        if not a[1].isdigit():
            ch1[int(a[0])] = int(a[2])
            ch2[int(a[0])] = int(a[3])
    res = []
    postorder(1)

    stack = []
    for i in res:
        if i.isdigit():
            stack.append(int(i))
        else:
            two = stack.pop()
            one = stack.pop()
            if i == '+':
                stack.append(one + two)
            elif i == '-':
                stack.append(one - two)
            elif i == '*':
                stack.append(one * two)
            elif i == '/':
                stack.append(one / two)

    print(f'#{tc} {int(stack[0])}')