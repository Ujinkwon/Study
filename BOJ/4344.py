t = int(input())


for i in range(t):
    cnt = 0
    arr = list(map(int, input().split()))
    average = sum(arr[1:])/arr[0]
    for j in arr[1:]:
        if j > average:
            cnt += 1

    print(f'{(cnt/arr[0]) * 100 :.3f}%')  # f'{변수:.3f}'  변수의 소수점 3자리까지만 출력

    