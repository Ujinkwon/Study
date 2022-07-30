num_list = []
for i in range(10):
    num_list.append(int(input()) % 42)

num_set = set(num_list)
print(len(num_set))
