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
    people = list(map(int, input().split()))
    people.sort()
    res = 'Possible'
    for i in range(n):
        cal = ((people[i] // m) * k - i - 1)
        if cal < 0:
            res = 'Impossible'
            break
    print(f'#{tc} {res}')


    # ret = '#'+str(tc)+' '+str(res)+'\n'
    # if ret != line[tc-1]:
    #     print(tc)

