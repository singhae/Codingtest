
def solution(left, right):
    answer = 0
    #약수구하기 
    #좌 ~ 우 구간까지 
    num = [] 
    for i in range(left,right+1):
        #print(left % i==0)
        #print("i is ",i)
        for j in range(1, i+1):
            #print("j is",j)
            if(i % j ==0):
                num.append(j)
        if len(num) % 2 == 0:
            answer += j
            num.clear()
        else:
            answer -= j
            num.clear()


    return answer
