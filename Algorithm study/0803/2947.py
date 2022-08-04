
def dd(list, i):
    if list[i] > list[i+1]:
        list[i], list[i+1] = list[i+1], list[i]
        print(*list)

list = list(map(int,input().split()))
a = [1, 2, 3, 4, 5]

while list!=a:
    for i in range(4):
        dd(list, i)
