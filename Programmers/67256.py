def solution(numbers, hand):
    answer = ''
    l, r = [1, 4, 7, 10], [3, 6, 9, 12]
    lpos, rpos = 10, 12
    d = [-3, 3, -1, 1]
    d2 = [-4, 4, -2, 2]
    for i in numbers:
        if i in l:
            answer += 'L'
            lpos = i
        elif i in r:
            answer += 'R'
            rpos = i
        else:
            pos = []
            if i == 0:
                i = 11
            for j in range(4):
                dpos = i + d[j]
                if 0 < dpos < 13:
                    pos.append(dpos)
                    
            
            if rpos in pos and lpos not in pos:
                answer += 'R'
                rpos = i
            elif lpos in pos and rpos not in pos:
                answer += 'L'
                lpos = i
            

        print(lpos, rpos, i)
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))