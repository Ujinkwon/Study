import sys
sys.stdin = open('2559.txt')

n, k = map(int, input().split())
arr = list(map(int, input().split()))
res = [sum(arr[:k])]
for i in range(n-k):
    res.append(res[i] - arr[i] + arr[k+i])
print(max(res))


# total = sum(arr[:k])
# s, e = 0, k
# max_value = -10000000
# while s < n-k+1 and e < n:
#     if total > max_value:
#         max_value = total
#     total -= arr[s]
#     total += arr[e]
#     s += 1
#     e += 1
# print(max_value)