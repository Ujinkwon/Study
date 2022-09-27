s = list(input())
s.append(2)
res = [0, 0]
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        res[int(s[i])] += 1
if sum(res) == 1:
    ans = 0
else:
    ans = min(res)
print(ans)