from audioop import reverse
import re


def solution(n, lost, reserve):
    answer = 0
    for i in lost:
        if i in reverse:
            reverse.remove(i)
    print(reserve)
    return answer

print(solution(5, [2,4], [1, 3, 5]))
print(solution(5, [2, 4], [2, 3]))
print(solution(5, [3], [1]))