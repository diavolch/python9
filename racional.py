from fractions import Fraction

def racional_result(a, b, move):
    res = 0
    a = Fraction(a.replace(' ', ''))
    b = Fraction(b.replace(' ', ''))
    if move == '+':
        res = a + b
    elif move == '-':
        res = a - b
    elif move == '*':
        res = a * b
    elif move == '/':
        res = a / b
    return res
