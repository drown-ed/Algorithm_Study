def solution(dots):
    arr = []
    answer = 0

    arr = dots[0]
    arr1 = dots[1]
    arr2 = dots[2]
    arr3 = dots[3]
    
    def cal_ab(x1,y1,x2,y2):
        a = (y2 - y1)/(x2 - x1)
        b = (x2*y1 - x1*y2)/(x2 - x1)

        return a, b
 
    return answer

dots = [[1, 4], [9, 2], [3, 8], [11, 6]]	

print(solution(dots))