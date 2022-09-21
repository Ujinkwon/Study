import sys, math
sys.stdin = open('1242.txt')

pattern = [
    [3,2,1,1],
    [2,2,2,1],
    [2,1,2,2],
    [1,4,1,1],
    [1,1,3,2],
    [1,2,3,1],
    [1,1,1,4],
    [1,3,1,2],
    [1,2,1,3],
    [3,1,1,2]
]

def hex_bin(n):
    res = ''
    h = 'ABCDEF'
    binary = ''
    for i in n:
        if len(res) == 4:
            binary += res[::-1]
            res = ''
        if i.isdigit():
            num = int(i)
        else:
            num = h.index(i)+10
        for j in range(4):
            res += str(num%2)
            num = num // 2
    binary += res[::-1]
    return binary

def ratio(nums):
    print(nums)
    cnt = 1
    res = []
    bit = []
    global arr
    for i in range(len(nums)-2, -1, -1):
        if len(res) == 7 and len(bit) == 3:
            l = (len(nums)-i-2)
            while l > 0:
                l = l-56
            cnt = -l
            print(i-l, nums[i-l])
            arr = nums[i-l]
            break
        if len(bit)==4:
            n = GCD(bit)
            if n > 1:
                for j in range(4):
                    bit[j] = bit[j] // n
            res.insert(0, bit)
            bit = []
        if nums[i] == nums[i+1]:
            cnt += 1
        else:
            bit.insert(0, cnt)
            cnt = 1
    bit.insert(0, cnt)
    n = GCD(bit)
    if n > 1:
        for i in range(4):
            bit[i] = bit[i]//n
    res.insert(0, bit)
    return res

def GCD(arr):
    ret = arr[0]
    for i in arr:
        ret = math.gcd(ret, i)
    return ret

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    a = [input() for _ in range(n)]
    a = list(set(a))
    arr = []
    for i in a:
        binary = ''
        for j in range(m):
            binary += hex_bin(i[j])
        arr.append(binary)
    check = []

    for i in arr:
        print(i)
    print()
    for i in range(len(arr)):
        for j in range(len(arr[0])-1, -1, -1):
            if arr[i][j] == '1':
                test = arr[i][:j+1]
                print(test)
                print(ratio(test))
    print(check)