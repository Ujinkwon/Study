arr = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()

time = 0
for i in arr:
    for j in i:
        for k in word:
            if k == j:
                time += (3 + arr.index(i))

print(time)