# Level 0 _ 다음에 올 숫자 .통과
def solution(common):
    common_len = len(common) # 최대 길이 변수 생성
    n = [0] * (len(common)+1) # 리스트 생성 +1 크기만큼   
    for i in range(len(common)): # 변수만큼 반복
        n[i] = common[i] # 리스트 복사
    if n[1]-n[0] == n[2]-n[1]: # 등차 수열 확인
        answer = n[common_len-1] + (n[2]-n[1]) # 다음 값 구하기
    elif n[1] // n[0] == n[2] // n[1]: # 등비 수열 확인
        answer = n[common_len-1] * (n[2] // n[1]) # 다음 값 구하기
    return answer

common = [2, 4, 8]	

print(solution(common))