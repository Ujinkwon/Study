def solution(numbers, hand):
    answer = ''
    lpos, rpos = 10, 12
    nums = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

    for i in numbers:
        if i == 0:
            i = 11
            
        if i in [1, 4, 7, 10]:
            answer += 'L'
            lpos = i
        elif i in [3, 6, 9, 12]:
            answer += 'R'
            rpos = i
        else:
            cnt_l, cnt_r = 0, 0
            for j in range(len(nums)):
                if lpos in nums[j]:
                    xl = nums[j].index(lpos)
                    yl = j
                if rpos in nums[j]:
                    xr = nums[j].index(rpos)
                    yr = j
                if i in nums[j]:
                    x = nums[j].index(i)
                    y = j
            cnt_l = abs(x-xl) + abs(y-yl)
            cnt_r = abs(x-xr) + abs(y-yr)

            if cnt_l < cnt_r or (cnt_l == cnt_r and hand == 'left'):
                answer += 'L'
                lpos = i
            elif cnt_l > cnt_r or (cnt_l == cnt_r and hand == 'right'):
                answer += 'R'
                rpos = i              
            
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))