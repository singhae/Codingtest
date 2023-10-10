def solution(a, b):
    answer = 1234567890
    count = 0
    for i in range(len(a)):
        count += a[i]*b[i]
        answer = count
    return answer
