def solution(board, moves):
    for i in range(len(board)):
        for j in range(len(board)):
            if i < j:
                board[j][i], board[i][j] = board[i][j], board[j][i]

    for i in board:
        while i[0] == 0:
            del i[0]
    
    box = []
    for k in moves:
        if k <= len(board) and board[k-1]:
            box.append(board[k-1][0])
            del board[k-1][0]
    
    stack = [0]
    answer = 0
    for i in range(len(box)-1):
        if box[i] != stack[-1]:
            stack.append(box[i])
        else:
            answer += 2
            stack.pop()
    return answer        


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))