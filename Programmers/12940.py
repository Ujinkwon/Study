def solution(n, m):
    answer = []
    for i in range(min(n,m), 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)             # 최대 공약수
            answer.append(n*m // i)      # 최대 공배수 = 두수의 곱 // 최대 공약수
            break
    return answer

print(solution(3,12))
print(solution(2,5))