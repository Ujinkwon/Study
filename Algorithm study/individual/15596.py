def solve(arr):              # 런타임에러 sum함수 사용이 시간짧게걸림
    total = 0
    for i in arr:
        total += i
    return total

def solve(arr):
    total = 0
    total = sum(arr)
    return total


arr = list(map(int, input().split()))
print(solve(arr))