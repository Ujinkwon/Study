n = input()
result = 0
cnt = 0

while cnt < 10:
    for i in n:
        result += int(i)

    n = n[len(n)-1] + str(result)[len(str(result))-1]
    cnt += 1

    print(str(result), n)
    if (str(result) == n):
        break

    result = 0
    

print(cnt)