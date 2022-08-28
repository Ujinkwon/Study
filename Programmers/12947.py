def solution(x):
    total = 0
    for i in str(x):
        total += int(i)
    return bool(x % total==0)

print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))