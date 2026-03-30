def solution(rsp):
    answer = ''
    for c in str(rsp):
        if c == '0':
            answer += '5'
        if c == '2':
            answer += '0'
        if c == '5':
            answer += '2'
    return answer