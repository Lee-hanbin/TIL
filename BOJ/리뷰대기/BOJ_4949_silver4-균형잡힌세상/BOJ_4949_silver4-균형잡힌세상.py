# BOJ_4949_silver4-균형잡힌세상


while 1:
    stack = [0]
    s = input()
    if s == '.':
        break
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
        elif i == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
    if len(stack) == 1:
        print('yes')
    else:
        print('no')