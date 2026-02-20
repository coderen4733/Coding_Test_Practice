def solution(n):
    pizza = 0
    while ((7 * pizza) / n) < 1:
        pizza = pizza + 1
    return pizza