def solution(board, skill):
    answer = 0
    check = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]

    for k in skill:
        if k[0] == 1:
            n = k[5]
        else:
            n = -k[5]
        check[k[1]][k[2]] += n
        check[k[3]+1][k[2]] -= n
        check[k[1]][k[4]+1] -= n
        check[k[3]+1][k[4]+1] += n

    for i in range(len(check)-1):
        for j in range(len(check[0])-1):
            check[i][j+1] += check[i][j]
    for i in range(len(check)-1):
        for j in range(len(check[0])-1):
            check[i+1][j] += check[i][j]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] - check[i][j] > 0:
                answer += 1
    return answer


print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))
print(solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))