def solution(babbling):
    babbling_list = ['aya', 'ye', 'woo', 'ma']
    temp_babbling = []
    answer = 0
    for i in range(babbling):
        for k in range(babbling_list):
            A = babbling_list[k]
            B = babbling[i]
            if A in B:
                temp_babbling.append(A)
                if babbling_list[k+1] in B:
                    temp_babbling.append(A)
                elif babbling_list[k+2] in B:
                    temp_babbling.append(A)
                elif babbling_list[k+3] in B:
                    temp_babbling.append(A)
        if temp_babbling[i] == B:
            answer += 1 
            
babbling = list(map(str, ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))

if __name__ == '__main__':
    print(solution(babbling))