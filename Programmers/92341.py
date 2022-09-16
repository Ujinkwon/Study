def solution(fees, records):
    answer = []
    lenght = len(records)
    arr = []
    totaltime = dict()
    for i in range(lenght):
        t, n, status = records[i].split()
        if status == 'IN':
            arr.append([n, t])
            if n not in totaltime.keys():
                totaltime[n] = []
        elif status == 'OUT':
            for i in range(len(arr)):
                if arr[i][0] == n:
                    totaltime[n].append(time_sum(arr[i][1], t))
                    arr.remove(arr[i])
                    break
    while arr:
        for i in range(len(arr)):
            totaltime[arr[i][0]].append(time_sum(arr[i][1], '23:59'))
            arr.remove(arr[i])
            break
    for i in totaltime.items():
        num, m = i
        totaltime[num] = money(sum(m), fees[0], fees[2]) * fees[3] + fees[1]
    answer = list(dict(sorted(totaltime.items())).values())
    return answer

def money(time, basictime, addt):
    time -= basictime
    res = time // addt
    if time % addt != 0:
        res += 1
    if time < 0:
        res = 0
    return res

def time_sum(i, o):
    ih, im = map(int, i.split(':'))
    oh, om = map(int, o.split(':'))
    if om < im:
        oh, om = oh-1, 60+om
    m = (oh-ih)*60 + (om-im)
    return m


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))