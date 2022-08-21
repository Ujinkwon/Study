n = int(input())
max_len = 0
for i in range(n // 2, n+1):
    one = n
    two = i
    three = one - two
    result = [one, two]

    while three > -1:
        three = one - two
        one = two
        two = three
        result.append(three)
        if max_len < len(result):
            max_len = len(result)
            ret = result
    print(result)

print(max_len-1)
print(*ret[:max_len-1])
