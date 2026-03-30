def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        new = []
        for j in range(n):
            new.append(num_list[i + j])
        answer.append(new)
    return answer
