import sys, math
sys.stdin = open('1242.txt')

# def scanner(arr):
#     total = 0
#     for row in range(n):
#         col = m * 4 - 1
#         while col >= 55:
#             if arr[row][col] == '1':
#                 for _ in range(8):
#                     n2 = n3 = n4 = 0
#                     while arr[row][col] == '1':
#                         n4 += 1
#                         col -= 1


t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    arr2 = [''] * n
    for i in range(n):
        temp = input()
        bit = ''
        for j in range(m):
            print( f'{int(temp[j], base=16):04b}')
            val = f'{int(temp[j], base=16):04b}'
            bit += val
        arr2[i] = bit
    print(arr2)