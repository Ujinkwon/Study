from re import L


t = int(input())

cnt, total = 0, 0
for i in range(t):
    ox = input()

    for j in range(len(ox)):
        if ox[j] == 'O':
            cnt = 1
            
            if j != 0 :
                for k in range(j, 0, -1):
                    if ox[k-1] == ox[k]:
                        cnt += 1
                    else:
                        break

        else:
            cnt = 0

        total += cnt
        cnt = 0

    print(total)
    total = 0
