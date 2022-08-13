n, k = map(int, input().split())
num = input()

# result = ''
# j = n - k
# list = []

# for i in range(j-1):
#         list.append(num[i])

# for i in range(j-1, len(num)):
#     print(num[i], i)
#     list.append(num[i])
#     result += max(list)
#     del list[list.index(max(list))]
  
    
# print(result)


list = []
for i in range(n): 
    while list and k > 0 and list[-1] < num[i]:  
        list.pop()   # 맨 뒷값 삭제
        k -= 1       # 지워야하는 수 k 감소

    list.append(num[i]) 

for i in list:
    print(i, end='')