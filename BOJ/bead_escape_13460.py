N, M = map(int, input().split())
for i in range(N):
    for j in range(M):
        if i == 0 or i == N-1:
            print('#', end = '')
        elif j == 0 or j == N-1:
            print('#', end = ' '*(M-2))
    print('\n')
