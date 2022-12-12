def solution(sizes):
    max_a, max_b = 0, 0

    for a, b in sizes:
        if a < b:
            a, b = b, a
        if max_a < a:
            max_a = a
        if max_b < b:
            max_b = b

    return max_a * max_b

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))