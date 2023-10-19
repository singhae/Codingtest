def solution(arr):
    answer = []
    
    print(len(arr))
    if len(arr) == 1: 
        answer = -1
    for i in range(len(arr)): 
        print(arr[i])
         
        # if arr[i] < arr[i+1]:
        #     answer[i] = arr[i+1]
        #     print(answer)
            
    
    return answer
