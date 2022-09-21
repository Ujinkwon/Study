import sys
sys.stdin = open('16987.txt')

def ff(idx, s):
    global res
    if idx == n:          # 가장 오른쪽 계란 들었으면 종료
        cnt = 0
        for i in range(n):  # 깨진 계란 카운트
            if s[i] <= 0:
                cnt += 1
        if cnt > res:   # 가장 많이 깬 계란 수로 업데이트
            res = cnt
        return

    if s[idx] <= 0:   # 손에 든 계란이 깨진 경우 넘어감
        ff(idx+1, s)
    else:
        for i in range(n):
            flag = 0
            if i != idx and s[i] > 0:  # 손에 든 계란으로 다른 계란들 치기
                temp = s[:]
                temp[i], temp[idx] = s[i]-w[idx], s[idx]-w[i]  # 내구도 - 무게
                flag = 1
                ff(idx+1, temp)  # 한 칸씩 이동하면서 계란 치기
        if flag == 0:  # 칠 계란이 없는 경우 넘어감
            ff(idx+1, s)

n = int(input())
s = [0]*n   # 내구도
w = [0]*n   # 무게
for i in range(n):
    s[i], w[i] = map(int, input().split())
res = 0
ff(0, s)
print(res)