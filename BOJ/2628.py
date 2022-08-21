r, c = map(int, input().split())
lx, rx, ly, ry = [0], [c], [0], [r]
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a == 0:
        lx.append(b)
        rx.append(b)
    else:
        ly.append(b)
        ry.append(b)
lx.sort()
rx.sort()
ly.sort()
ry.sort()

x_gap, y_gap = 0, 0
for i in range(len(lx)):
    if rx[i] - lx[i] > x_gap:
        x_gap = rx[i] - lx[i]
for j in range(len(ly)):
    if ry[j] - ly[j] > y_gap:
        y_gap = ry[j] - ly[j]
print(x_gap * y_gap)