def solution(n):
    answer = ''
    letter_0 = '박'
    letter_1 = '수'
    for i in range(1,n+1):
        #print(i)
        if i % 2 != 0 : 
            answer += letter_1
        else: 
            answer += letter_0
        
    return answer
