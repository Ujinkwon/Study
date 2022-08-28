def solution(strings, n):
    return sorted(sorted(strings), key =lambda x : x[n])
# key를 가지는 sort함수 => key 기준으로 정렬 

print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))