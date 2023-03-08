def solution(num):
    odd = 'Odd'
    even = 'Even'
    if num % 2 == 0:
        answer = even
        return answer
    elif num % 2 != 0:
        answer = odd
        return answer
    return answer