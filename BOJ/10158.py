w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

x = (p + t) % (2 * w)
y = (q + t) % (2 * h)

if x > w:
    x = w - (x % w)
if y > h:
    y = h - (y % h)

print(x, y)

# 0,1,2,3,4,5,6,5,4,3,2,1
# 0,1,2,3,4,3,2,1
