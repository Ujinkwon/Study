import sys
sys.stdin = open('1860.txt')

# f = open('test.txt', 'r')
# line = []
# for i in range(1000):
#     line.append(f.readline())
# f.close

t = int(input())
for tc in range(1, t+1):
    n, m, k = map(int, input().split())
    narr = list(map(int, input().split()))
    narr.sort()

    if narr[0] % m:
            narr[0] -= 1
    total = ((narr[0]//m) * k) -1
    if total < 0:
        res = 'ImPossible'
    else:   
        res = 'Possible'
        for i in range(1, n):
            if narr[i] % m:
                narr[i] -= 1
            total += (((narr[i] - narr[i-1])//m) * k) -1
            if total < 0:
                res = 'Impossible'
                break
    
    print(f'#{tc} {res}')




    # ret = '#'+str(tc)+' '+str(res)+'\n'
    # if ret != line[tc-1]:
    #     print(tc)

