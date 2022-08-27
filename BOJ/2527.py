import sys
sys.stdin = open('2527.txt')

for _ in range(4):
    lx1, ly1, rx1, ry1, lx2, ly2, rx2, ry2 = map(int, input().split())
    if lx1 > lx2: 
        lx1, ly1, rx1, ry1, lx2, ly2, rx2, ry2 = lx2, ly2, rx2, ry2, lx1, ly1, rx1, ry1

    if (rx1 == lx2) and ((ry1 == ly2) or (ly1 == ry2)):
        res = 'c'
    elif (rx1 < lx2) or (ry1 < ly2) or (ly1 > ry2):
        res = 'd'
    elif ((lx2 < rx1) and ((ly1 == ry2) or (ry1 == ly2))) or ((rx1 == lx2) and ((ry1 > ly2) or (ry2 > ly1))):
        res = 'b'
    else:
        res = 'a'
    print(res)
