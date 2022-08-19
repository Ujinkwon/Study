n = int(input())
result  = 0
for i in range(n):
    char = input()
    l = []
    for c in range(len(char)):
        if char[c] not in l:
            l.append(char[c])
            cnt = 1
        else:
            if char[c-1] != char[c]:
                cnt = 0
                break
    result += cnt
print(result)