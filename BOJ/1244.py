def change(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0
    return


N = int(input())
switch = [-1] + list(map(int, input().split()))  #인덱스를 1부터 보기 위함
students = int(input())
for _ in range(students):
    sex, num = map(int, input().split())

    # 남자
    if sex == 1:
        for i in range(num, N+1, num): #범위 내의 배수만 
            change(i)
    # 여자
    else:
        change(num)
        for k in range(N//2):   #대칭이니까 반틈만
            if num + k > N or num - k < 1 : break  # 범위를 벗어나는 대칭일 경우 (이 조건 없으면 런타임 에러 발생)

            if switch[num + k] == switch[num - k]:
                change(num + k)
                change(num - k)
            else:
                break
                
for i in range(1, N+1):
    print(switch[i], end = " ")
    if i % 20 == 0 :    #스무개 단위로 끊어서 출력
        print()




# import sys

# n = int(sys.stdin.readline())
# status = list(map(int, sys.stdin.readline().split()))
# student = int(sys.stdin.readline())

# for i in range(student):
#     data = list(map(int, sys.stdin.readline().split()))

#     if data[0] == 1:
#         for i in range(1, len(status)+1):
#             if i % data[1] == 0:
#                 if status[i-1] == 0:
#                     status[i-1] = 1
#                 else:
#                     status[i-1] = 0

#     elif data[0] == 2:
#         if status[data[1]-1] == 0:
#             status[data[1]-1] = 1
#         else:
#             status[data[1]-1] = 0

#         for i in range(1, data[1]):
#             if status[data[1]-1-i] == status[(data[1]-1) + i]:
#                 if status[data[1]-1-i] == 0:
#                     status[data[1]-1-i] = 1
#                 elif status[data[1]-1-i] == 1:
#                     status[data[1]-1-i] = 0

#                 if status[data[1]-1+i] == 0:
#                     status[data[1]-1+i] = 1
#                 elif status[data[1]-1+i] == 1:
#                     status[data[1]-1+i] = 0
#             else:
#                 break

# for i in status:
#     print(i, end=" ")
