def solution(new_id):
    # 소문자 치환
    new_id = new_id.lower()
    id = []

    # 사용 불가한 문자 제거
    for i in new_id:
        if i.islower() == True or i.isdigit() == True or i == '-' or i == '_' or i == '.':
           id.append(i)    

    # 마침표 연속 부분 변경
    stack = [0]
    for j in range(len(id)):
        if stack[-1] == '.' and id [j] == '.':
            pass
        else:
            stack.append(id[j])
    stack = stack[1:]

    # 마침표 불가능 위치 제거
    if stack[0] == '.':
        stack.pop(0)
    elif stack[-1] == '.':
        stack.pop()

    # 빈문자열 => a 삽입
    if not stack:
        stack.append('a')
    
    # 글자수 15개 제한
    if len(stack) > 15:
        stack = stack[:15]

    # 마침표 불가능 위치 제거
    if stack[0] == '.':
        stack.pop(0)
    elif stack[-1] == '.':
        stack.pop()

    # 최소길이 3
    while len(stack) < 3:
        stack.append(stack[-1])

    answer = ''
    for k in stack:
        answer += k
    return answer

print(solution('...!@BaT#*..y.abcdefghijklm'))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))


# 정규식 !!!!!!!!!!!!!!!!!!
# import re

# def solution(new_id):
#     st = new_id
#     st = st.lower()
#     st = re.sub('[^a-z0-9\-_.]', '', st)
#     st = re.sub('\.+', '.', st)
#     st = re.sub('^[.]|[.]$', '', st)
#     st = 'a' if len(st) == 0 else st[:15]
#     st = re.sub('^[.]|[.]$', '', st)
#     st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
#     return st