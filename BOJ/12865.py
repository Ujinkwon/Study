import sys

n, k = map(int, input().split())

w_list, v_list = [], []
v_set = set()
for i in range(n):
    w, v = map(int, sys.stdin.readline().split())
    w_list.append(w)
    v_list.append(v)

for i in range(len(w_list)):
    for j in range(1, len(w_list)):
        if w_list[i] + w_list[j] == k:
            v_set.add(v_list[i] + v_list[j])
            
print(max(v_set))