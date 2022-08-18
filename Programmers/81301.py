def solution(s):
    nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(len(nums)):
        if nums[i] in s:
            s = s.replace(nums[i], str(i))

    answer = int(s)
    return answer

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))