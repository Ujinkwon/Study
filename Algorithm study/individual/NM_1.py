N, M = map(int, input().split())
s = []                  # 재귀함수를 이용해 M개의 수열을 저장하기 위한 리스트

def dfs():
    if len(s) == M :    # 리스트에 들어간 수열들이 M개가 되면 출력
        print(' '.join(map(str,s)))
    
    for i in range(1, N+1):   
        if i not in s:        # 리스트 S 중복 여부 확인
            s.append(i)       # 중복이 아니면 리스트에 추가
            dfs()             # 현재 s=[1]인 상태에서 다음숫자를 넣기 위해 가지치기하기(재귀함수)
            s.pop()           # 만약 N=4, M=2이면 
                              # [1]=>[1,2]=>[1]=>[1,3]=>[1]=>[1.4]

dfs()