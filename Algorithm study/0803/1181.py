n = int(input())

word_list = []
for i in range(n):
    word_list.append(input())

word_list = list(set(word_list))
list2 = sorted(word_list)
ret = sorted(list2, key=lambda x : len(x), reverse= False)

for i in ret:
    print(i)
