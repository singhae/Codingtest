
def solution(n, m, section):
    answer = 0
    

# #section 끝이랑 첫번째랑 빼서 +1 을 한게 m 보다 크면 m을 한번 더 해 -> 큰 값에다가  m을 나눠

#     block = section[-1] - section[0] + 1
#     #print(block)
#     paint = block / m 
#     #print(paint)
#     #paint 값이 block보다
#     if block < m: 
#         answer = 1
#     elif block == round(paint):
#         answer = block
#     else: 
#         answer = round(paint) + 1
#         #print(paint)
#     #print(paint)
    
    #최대값
    max = 0 
    #최대값보다 
    len_section = len(section)
    for i in range(0,len_section): #빈벽시작점 ~ 빈벽 끝점
        if(section[i] < max):
            continue
        
        answer += 1
        max = section[i] + m 
        
    return answer