# Level 0 _ 평행 _ 해결
def solution(dots):
    answer = 0

    def cal_ab(x1, y1,x2, y2): # 기울기 공식
        a = (y2 - y1)/(x2 - x1)
        return a
    # 2차원 배열 요소 뽑아서 기울기 비교
    if cal_ab(dots[0][0],dots[0][1],dots[1][0],dots[1][1]) == cal_ab(dots[2][0],dots[2][1],dots[3][0],dots[3][1]):
        answer = 1 
    elif cal_ab(dots[0][0],dots[0][1],dots[2][0],dots[2][1]) == cal_ab(dots[1][0],dots[1][1],dots[3][0],dots[3][1]):
        answer = 1
    elif cal_ab(dots[0][0],dots[0][1],dots[3][0],dots[3][1]) == cal_ab(dots[1][0],dots[1][1], dots[2][0],dots[2][1]):
        answer = 1
    else:
        answer = 0
    return answer

dots = [[1, 4], [9, 2], [3, 8], [11, 6]]	

print(solution(dots))