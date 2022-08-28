def solution(n):
    arr = set(range(2,  n+1))
    for i in range(2, n+1):   #배수 삭제
        arr -= set(range(2*i, n+1, i))
    return len(arr)

# def solution(n):
#     answer = 0
#     for i in range(2, n+1):    #소수 찾기
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             answer += 1
#     return answer

print(solution(10))
print(solution(5))