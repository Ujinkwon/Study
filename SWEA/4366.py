import sys
sys.stdin = open('4366.txt')

t = int(input())
for tc in range(1, t+1):
    binary = input()
    three = input()
    bin_dec = []
    for i in range(len(binary)):
        temp = list(binary[:])
        if binary[i] == '1':
            temp[i] = '0'
        else:
            temp[i] = '1'
        num = ''.join(s for s in temp)
        bin_dec.append(int(num, 2))
    flag = 0
    for i in range(len(three)):
        temp = list(three[:])
        for j in range(3):
            if three[i] != j:
                temp[i] = str(j)
                num = ''.join(s for s in temp)
                if int(num, 3) in bin_dec:
                    res = int(num, 3)
                    flag = 1
                    break
        if flag == 1:
            break

    print(f'#{tc} {res}')