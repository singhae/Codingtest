def solution(s):
    answer = ''
    len_s = int(len(s) / 2)
    if len(s) % 2 != 0: 
        answer = s [len_s]
        
    else:
        answer = s[len_s-1:len_s+1] #[:여기값은 +1]
    
    return answer
