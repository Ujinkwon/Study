word = input().lower()
arr = list(set(word))
cnt_arr = []

for i in arr:
    cnt = word.count(i)
    cnt_arr.append(cnt)

if cnt_arr.count(max(cnt_arr)) >= 2:
    print('?')
else:
    print(arr[cnt_arr.index(max(cnt_arr))].upper())