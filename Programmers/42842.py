def solution(brown, yellow):
    for i in range(1, yellow+1):
        if yellow % i == 0:
            a, b = i+2, (yellow//i)+2
            # print(a, b)
            if (a*b - yellow) == brown:
                break
    return [b, a]


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))