def solution(numbers):
    answer = -1
    count = 0

    for i in range(0,10):
        if i not in numbers:
            print(i)
            count += i
    answer = count
    return answer
