def solution(name, yearning, photo):
    answer = []
    dict = {}
    for a, b in zip(name,yearning): 
        dict[a] = b

    for case in photo:
        tmp = 0 
        for i in range(len(case)):
            if case[i] in dict:
                tmp += dict[case[i]]
                #print(tmp)
            else:
                continue
        answer.append(tmp)
    return answer