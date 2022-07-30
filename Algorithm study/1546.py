n = int(input())

num_list = list(map(int, input().split()))
print(num_list[0])

new_list = []

num_max = num_list[0]

for i in num_list:
    print(i, type(i))
    if num_max < int(i):
        num_max = i

for i in num_list:
    new_list.append(int(i) / num_max * 100)

print(sum(new_list)/len(new_list))