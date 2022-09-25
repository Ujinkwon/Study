# 조합 (중복 x, 순서 x)
def combi(arr, n):
    result = []
    if n > len(arr):
        return result
    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr)-n+1):
            for j in combi(arr[i+1:], n-1):
                result.append([arr[i]]+j)
    return result

def perm(arr, n):
    result = []
    if n > len(arr):
        return result
    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr)):
            ans = [i for i in arr]
            ans.remove(arr[i])
            for j in perm(ans, n-1):
                result.append([arr[i]]+j)
    return result

arr = [1,2,3,4,5]
print(combi(arr, 8))
print(perm(arr, 5))