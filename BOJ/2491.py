n = int(input())
arr = list(map(int, input().split()))
arr2 = arr
lenght = []
while len(arr) > 2:
    cnt = 0
    min_num = arr[0]
    for i in range(len(arr)):
        if min_num <= arr[i]:
            min_num = arr[i]
            cnt += 1
        else:
            arr = arr[i:]
            break
    lenght.append(cnt)

arr = arr2
while len(arr) > 2:
    cnt2 = 0
    max_num = arr[0]
    for j in range(len(arr)):
        if max_num >= arr[j]:
            max_num = arr[j]
            cnt2 += 1
        else:
            arr = arr[j:]
            break
    print(arr[j:])
    lenght.append(cnt2)

print(lenght)