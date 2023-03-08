def solution(n):
    answer = 0
    word = list(str(n))

    for i in range(len(word)):
        answer += int(word[i])
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    return answer

if __name__ == '__main__':
    print(solution(987))