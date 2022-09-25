import sys
sys.stdin =open('1952.txt')

t = int(input())
for tc in range(1, t+1):
    day, month, three_month, year = map(int, input().split())
    plan = list(map(int, input().split()))
    arr = [0]*12
    arr3 = [0]*12
    # 1일 이용권 vs 한달 이용권
    for i in range(12):
        if plan[i]*day <= month:
            arr[i] = plan[i]*day
        else:
            arr[i] = month

    # vs 세달 이용권
    three_vs = sum(arr)
    for j in range(12):
        arr2 = arr[:]
        for i in range(j, 12):
            if i == 10 and arr2[i] + arr2[i+1] > three_month:
                arr2[i] = three_month
                arr2[i+1] = 0
            elif i == 11 and arr2[i] > three_month:
                arr2[i] = three_month
            elif 0 <= i < 10 and arr2[i]+arr2[i+1]+arr2[i+2] > three_month:
                    arr2[i] = three_month
                    arr2[i+1] = arr2[i+2] = 0
        if sum(arr2) < three_vs:
            three_vs = sum(arr2)

    # vs 1년 이용권
    if three_vs > year:
        ans = year
    else:
        ans = three_vs

    print(f'#{tc} {ans}')

    # price = list(map(int, input().split()))
    # plan = list(map(int, input().split()))
    # arr = [0]*13
    # three_month = 36001
    # for i in range(1,13):
    #     day = plan[i-1] * price[0] + arr[i-1]
    #     month = price[1] + arr[i-1]
    #     if i > 2:
    #         three_month = price[2] + arr[i-3]
    #     arr[i] = min(day, month, three_month)
    # print(f'#{tc} {min(arr[12], price[3])}')

