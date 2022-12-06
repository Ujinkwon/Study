from collections import deque

def solution(maps):
    q = deque()
    q.append((0, 0))
    xl, yl = len(maps), len(maps[0])

    while q:
        x, y = q.popleft()
        for i in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            dx, dy = x+i[0], y+i[1]
            if 0 <= dx < xl and 0 <= dy < yl and maps[dx][dy] == 1:
                maps[dx][dy] = maps[x][y] + 1
                q.append((dx, dy))

    # print(maps)
    if maps[xl-1][yl-1] == 1:
        return -1
    return maps[xl-1][yl-1]


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))