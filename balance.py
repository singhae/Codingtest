import sys

while True:
    #input = sys.stdin.readline() #엔터마다 끊어줘야함 
    input1 = input()
    if input1 == '.' : 
        break
    stack = []
    stack1 = []

    for i in input1:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break

    if len(stack) == 0 : print('yes')
    else: print('no')