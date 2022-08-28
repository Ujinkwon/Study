# def solution(d, budget):
#     arr = []
#     for i in range(1 << len(d)):
#         total, cnt = 0, 0
#         for j in range(len(d)):
#             if i & (1<<j):
#                 total += d[j]
#                 cnt += 1
#         if total == budget:
#             arr.append(cnt)
#     return max(arr)

def solution(d, budget):
    d.sort()
    total, cnt = 0, 0
    for i in range(len(d)):
        total += d[i]
        if total > budget:
            break
        cnt += 1
    return cnt

print(solution([1,3,2,5,4],9))
print(solution([2,2,3,3],10))