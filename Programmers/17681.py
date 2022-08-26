def solution(n, arr1, arr2):
    answer = [''] * n
    arr = [[0]*n for _ in range(n)]
    new_arr, new_arr2 = [], []
    for i in range(n):
        new_arr.append(binary(n, arr1[i], []))
    for i in range(n):
        new_arr2.append(binary(n, arr2[i], []))
        
    for i in range(n):
        for j in range(n):
            if arr[i][j] != new_arr[i][j]:
                answer[i] += '#'
            elif arr[i][j] != new_arr2[i][j]:
                answer[i] += '#'
            else:
                answer[i] += ' '

    return answer

def binary(n, number, arr):
    while number != 0:
        arr.append(number % 2)
        number = number // 2
    while len(arr) != n:
        arr.append(0)
    return arr[::-1]

print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))
print(solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]))
