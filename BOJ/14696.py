t = int(input())
for _ in range(t):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(4, 0, -1):
        cnt_a, cnt_b = 0, 0
        for j in a[1:]:
            if j == i:
                cnt_a += 1
        for k in b[1:]:
            if k == i:
                cnt_b += 1
        
        if cnt_a > cnt_b:
            result = 'A'
            break
        elif cnt_a < cnt_b:
            result = 'B'
            break
    else:
        result = 'D'

    print(result)