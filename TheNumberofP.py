def solution(s):
    answer = True
    p = 0
    y = 0 
    s = s.lower()
    print(s)
    for i in s: 
        #print(i)
        if i in 'p':
            #print("p")
            #print(p+1)
            p +=1
        elif i in 'y':
            #print("y")
            y +=1
        else:
            continue

    if p == y: 
        answer = True
    else:
        answer = False
            
    return answer
