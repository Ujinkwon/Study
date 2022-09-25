import sys
sys.stdin = open('4.txt')

def postorder(n):
    global cal
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        cal.append(arr[n])

for _ in range(10):
    n = int(input())
    ch1 = [0]*(n+1)
    ch2 = [0]*(n+1)
    arr = [0]*(n+1)
    for i in range(n):
        a = list(input().split())
        for j in range(2, len(a)):
            p, c = int(a[0]), int(a[j])
            if ch1[p] == 0:
                ch1[p] = c
            else:
                ch2[p] = c
        arr[int(a[0])] = a[1]
    cal = []
    postorder(1)
    stack = []
    for i in cal:
        if i.isdigit():
            stack.append(int(i))
        else:
            one = stack.pop()
            two = stack.pop()
            if i == '+':
                stack.append(two + one)
            elif i == '-':
                stack.append(two - one)
            elif i == '*':
                stack.append(two * one)
            elif i == '/':
                stack.append(two // one)
    print(stack[0])