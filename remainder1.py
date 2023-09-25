def solution(n):
    answer = 0
    print(n)
    for x in range(1,1000000):
        if n % x != 1:
            #print(x)
            continue
        else:
            #print(x)
            answer = x
            break
    return answer
