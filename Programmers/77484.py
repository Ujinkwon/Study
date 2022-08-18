from multiprocessing.util import log_to_stderr


def solution(lottos, win_nums):
    cnt = 0
    for i in lottos:
        if i in win_nums:
            cnt += 1
    result = [7 - (lottos.count(0) + cnt), 7 - (cnt)]

    if result[0] > 5:
        result[0] = 6
    if result[1] > 5:
        result[1] = 6
    answer = result
    return answer


lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]
print(solution(lottos, win_nums))