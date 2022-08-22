n = int(input())
arr = list(map(int, input().split()))
stack1, stack2 = [0]*n, [0]*n
result = 0
for i in range(1, n):
    if arr[i] >= arr[i-1]:
        stack1[i] += stack1[i-1] +1

    if arr[i] <= arr[i-1]:
        stack2[i] += stack2[i-1] +1

print(max(max(stack1), max(stack2))+1)