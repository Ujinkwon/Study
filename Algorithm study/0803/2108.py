import sys

n = int(input())

list = []
for i in range(n):
    list.append(int(sys.stdin.readline()))
list2 = sorted(list)

cnt_list = []
list3 = []
for i in set(list):
    cnt_list.append(list.count(i))
    list3.append(i)


if cnt_list.count(max(cnt_list)) > 1:
    max_cnt = sorted(cnt_list)[1]
    max_cnt = list3[cnt_list.index(max_cnt)]
else:
    max_cnt = list3[cnt_list.index(max(cnt_list))]

print(round(sum(list)/len(list)))
print(list2[len(list)//2])
print(max_cnt)
print(max(list)-min(list))

# import sys
# from collections import Counter
# n = int(sys.stdin.readline())
# nums = []
# for i in range(n):
#     nums.append(int(sys.stdin.readline()))
# nums.sort()
# nums_s = Counter(nums).most_common()
# print(round(sum(nums) / n))
# print(nums[n // 2])
# if len(nums_s) > 1:
#     if nums_s[0][1] == nums_s[1][1]:
#         print(nums_s[1][0])
#     else:
#         print(nums_s[0][0])
# else:
#     print(nums_s[0][0])
# print(nums[-1] - nums[0])