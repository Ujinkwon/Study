def combi(arr, n):
    result =[] 
    if n == 0: 
        return [[]]

    for i in range(0, len(arr)): 
        elem = arr[i] 
        rest_arr = arr[i + 1:] 
        for C in combi(rest_arr, n-1): 
            result.append([elem]+C) 
    return result


array = [int(input()) for _ in range(9)]
for i in combi(array, 7):
    total = 0
    for j in i:
        total += j
    if total == 100:
        result = i
        break
while result:
    min_value = 100
    for k in result:
        if min_value > k:
            min_value = k
    print(min_value)
    result.remove(min_value)
    
        