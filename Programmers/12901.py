def solution(a, b):
    day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    m = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    idx = (sum(m[:a-1]) + b) % 7
    return day[idx]

print(solution(5,24))
print(solution(1,1))