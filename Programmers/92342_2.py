from itertools import combinations_with_replacement

def solution(n, info):
    max_value = 0
    res = []
    for combi in combinations_with_replacement(range(11), n):
    # 라이언이 n발을 쏘는 과녁의 경우들
        lion = [0]*11
        apeach_cnt, lion_cnt = 0, 0
        for i in combi:   # 라이언 배열에 개수 업데이트
            lion[i] += 1
        for j in range(11):   # 어피치와 라이언 각각 점수 계산
            if (info[j] > lion[j]) or (info[j] == lion[j] and info[j] != 0):
                apeach_cnt += (10-j)
            elif info[j] < lion[j]:
                lion_cnt += (10-j)
        gap = lion_cnt - apeach_cnt
        if gap > 0:   # 라이언이 이기는 경우
            if max_value < gap:    # 현재의 최댓값보다 더 큰 점수차가 있다면 업데이트 후, 저장배열 리셋
                res = [[lion, combi]]
                max_value = gap
            elif max_value == gap:  # 점수차가 최댓값과 같을 경우, 배열 추가
                res.append([lion, combi])
    if len(res) == 1:
        answer = res[0][0]
    elif not res:
        answer = [-1]
    else:   # 가장 큰 점수 차로 이길 수 있는 방법이 여러개인 경우
        new_res = []   # 다음 최소값 비교 위해 업데이트 해줄 배열 생성
        for i in range(10, -1, -1):  # 거꾸로 돌려가면서 개수 비교
            max_cnt = -1
            for k in res:
                if k[1].count(i) > max_cnt:
                    max_cnt = k[1].count(i)
                    new_res = [k]
                elif k[1].count(i) == max_cnt:
                    new_res.append(k)
            if len(new_res) == 1:   # 개수가 가장 많은게 하나면 해당 라이언 배열 출력
                answer = new_res[0][0]
                break
            else:   # 개수 같은게 여러개면 새로 담은 배열로 업데이트
                res = new_res[:]
    return answer



print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))