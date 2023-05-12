def solution(name, yearning, photo):
    add = 0
    answer = []
    my_dict= {}
    for name, yearning in zip(name, yearning):
        my_dict[name] = yearning

    for i in range(0, len(photo)):
        for j in photo[i]:
            try:
                if(my_dict[j] != None):
                    add += my_dict[j]
            except:
                continue
        answer.append(add)
        add = 0

    return answer

