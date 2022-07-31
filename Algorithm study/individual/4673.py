def self_num():
    arr = []
    for i in range(10001):
        total = 0
        for j in str(i):
            total += int(j)
        arr.append(total + i)

    for k in range(10001):
        if k not in arr:
            print(k)


self_num()
            