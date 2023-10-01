def solution(num):
    answer = 0
    count = 0
    for i in range(500):
        if num != 1: 
            if num % 2 == 0:
                num = num / 2
                count += 1
            elif num % 2 != 0: 
                num = num * 3 + 1
                count += 1

    if count >= 500: 
        answer = -1 
    else:
        answer = count 
    return answer
