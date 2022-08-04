n = int(input())

list = []
for i in range(n):
    list.append(int(input()))

cnt = []
new_list = []
for i in set(list):
    cnt.append(list.count(i))
    new_list.append(i)

print(new_list[new_list.index(max(cnt))])