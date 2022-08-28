def solution(price, money, count):
    total = price * sum(list(range(count+1)))
    if money < total:
        return total - money
    else:
        return 0

print(solution(3,20,4))