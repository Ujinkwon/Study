from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    visited = [0]*len(words)
    q = deque()
    q.append((begin, 0))
    while q:
        word, res = q.popleft()
        if word == target:
            break
        else:
            for i in range(len(words)):
                if not visited[i]:
                    cnt = 0
                    for j in range(len(target)):
                        if word[j] != words[i][j]:
                            cnt += 1
                    if cnt == 1:
                        visited[i] = 1
                        q.append((words[i], res+1))
    return res


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))