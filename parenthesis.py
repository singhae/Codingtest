import sys

t = int(sys.stdin.readline())

#total = 0
for i in range(t):
    p = sys.stdin.readline()
    stack = []
    # a = p.count('(')
    # b = p.count(')')
    # if a != b: 
    #     print("NO")
    # else:
    for n in p:
        if n == '(':
            #total += 1
            stack.append('(')
        elif n == ')':
            #total -= 1
            #if total == -1:
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
        #if total == 0:
    if len(stack) == 0:
        print("YES")
    else: print("NO")
