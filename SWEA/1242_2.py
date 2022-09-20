import sys, math
sys.stdin = open('1242.txt')

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
    cnt = 1
    res = []
    bit = []
    for i in range(len(nums)-1):
        if len(bit)==4:
            n = GCD(bit)
            if n > 1:
                for j in range(4):
                    bit[j] = bit[j] // n
            res.append(bit)
            bit = []
        if nums[i] == nums[i+1]:
            cnt += 1
        else:
            bit.append(cnt)
            cnt = 1
    bit.append(cnt)
    n = GCD(bit)
    if n > 1:
        for i in range(4):
            bit[i] = bit[i]//n
    res.append(bit)
    return res


def GCD(arr):
    ret = arr[0]
    for i in arr:
        ret = math.gcd(ret, i)
    return ret

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

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    idx = []
    for i in range(1, n):
        for j in range(1, m):
            if arr[i][j] != '0' and arr[i][j-1] == '0' and arr[i-1][j]=='0':
                if (j-3 >= 0 and arr[i][j-2] == '0' and arr[i][j-3]) or j-3 < 0:
                        idx.append([i, j])
                
    print(idx)
    ans = 0
    for k in idx:
        y, x = k[0], k[1]
        for i in range(x, len(arr[y])-1):
            if arr[y][i] == '0' and arr[y][i+1]== '0':
                x2 = i
                break
        else:
            x2 = len(arr[y])-1

        print(arr[y][x:x2])
        num = '0000'*x
        for i in arr[y][x:x2]:
            num += hex_bin(i)
        for i in range(len(num[::-1])-1, -1, -1):
            if num[i] == '1':
                num = num[0:i+1]
                break
        for i in range(len(num)):
            if num[i] == '1':
                num = num[i:]
                break
        if len(num) % 56 :
            num = num[::-1]
            num += '0' * (8 - (len(num) % 8))
            num = num[::-1]


        odd = even = 0
        a = ratio(num)
        for i in range(len(a)):
            if i % 2:
                even += pattern.index(a[i])
            else: 
                odd += pattern.index(a[i])

        if (odd*3 + even) % 10 == 0:
            ans += odd+even

    print(f'#{tc} {ans}')