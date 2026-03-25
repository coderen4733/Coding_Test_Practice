def solution(age):
    pg = "abcdefghij"
    answer = ''
    for c in str(age):
        answer = answer + pg[int(c)]
    return answer