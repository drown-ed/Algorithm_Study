def solution(babbling):
    check_list = ["aya", "ye", "woo", "ma"]
    answer = 0
    for i in range(len(babbling)):
        BB = babbling[i]        
        for j in range(4):
            CL = check_list[j]
            if CL in BB:
                BB = BB.replace(CL,' ')
                babbling[i] = BB
            elif BB > '':
                pass
        if babbling[i].strip() == '':
            answer += 1
        else:
            continue
    return answer