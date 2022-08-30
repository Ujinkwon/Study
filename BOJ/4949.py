while 1:
    word = (input())
    if word == '.':
        break
    
    stack = []
    for i in range(len(word)):
        if word[i] == '(' or word[i] == '[':
            stack.append(word[i])
        
        if len(stack) != 0:
            if word[i] == ')' and stack[-1] == '(':
                stack.pop()
            if word[i] == ']' and stack[-1] == '[':
                stack.pop()
    if len(stack) == 0:
        res = 'yes'
    else:
        res = 'no'
    print(res)