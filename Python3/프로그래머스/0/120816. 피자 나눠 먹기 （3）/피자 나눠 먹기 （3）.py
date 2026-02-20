def solution(slice, n):
    pizza = 0
    while ((pizza * slice) / n) < 1:
        pizza = pizza + 1
    return pizza