from itertools import permutations
import math

def solution(numbers):
    answer = set()
    
    def isPrime(number):
        for i in range(2, int(math.sqrt(number))+1):
            if number % i == 0:
                return False
            return True

    for i in range(1, len(numbers)+1):
        temp = set(map(''.join, permutations(numbers, i)))
        for j in temp:
            num = int(j)
            if isPrime(num):
                answer.add(num)

    return len(answer)

print(solution("17"))
print(solution("011"))