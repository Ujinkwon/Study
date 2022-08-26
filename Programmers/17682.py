def solution(dartResult):
    step, ret = [], [0]*3
    s = 0
    for i in range(1, len(dartResult)-1):
        if dartResult[i].isdigit():
            e = i
            if dartResult[i-1].isdigit():
                e = i-1
                continue
            step.append(dartResult[s:e])
            s = i
    step.append(dartResult[e:])

    for i in range(3):
        if len(step[i]) == 2:
            ret[i] = int(step[i][0]) ** bonus(step[i][1])
        elif len(step[i]) >= 3:
            if step[i][1].isdigit():
                ret[i] = (int(step[i][0] + step[i][1])) ** bonus(step[i][2])
            else:
                ret[i] = int(step[i][0]) ** bonus(step[i][1])

        if len(step[i]) >= 3:
            if step[i][-1] == '#':
                ret[i] *= -1
            elif step[i][-1] == '*':
                ret[i] *= 2
                if i > 0:
                    ret[i-1] *= 2
                    
    return (sum(ret))

def bonus(char):
    if char == 'S':
        ret = 1
    elif char == 'D':
        ret = 2
    else:
        ret = 3
    return ret

print(solution('1S2D*3T'))
print(solution('1D2S#10S'))
print(solution('1D2S0T'))
print(solution('1S*2T*3S'))
print(solution('1D#2S*3S'))
print(solution('1T2D3D#'))
print(solution('1D2S3T*'))