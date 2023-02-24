# Level 0 _ 옹알이 통과
def solution(babbling):
    check_list = ["aya", "ye", "woo", "ma"] # 비교값
    answer = 0  # 정답 개수
    for i in range(len(babbling)):  # 입력값 만큼 반복
        BB = babbling[i] # 입력값 대입
        for j in range(4):  # 비교값 만큼 반복
            CL = check_list[j]  # 비교값 대입
            if CL in BB: # 비교값이 대입값 안에 존재한다면
                BB = BB.replace(CL,' ') # 비교값을 ' '으로 치환하여 대입
                babbling[i] = BB # 대입 값을 원래 리스트에 반환
            elif BB > '': # 만약 BB가 빈 리스트가 아니라면
                pass    # 무시
        if babbling[i].strip() == '':   # 아까 넣어준 빈 ' '값을 지웠더니 빈칸이라면
            answer += 1 # 정답 1증가
        else:
            continue    # 아니면 컨티뉴
    return answer # 정답 반환