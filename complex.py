def complex_result(a, b, move):
    res = 0
    a = complex(a.replace(' ', ''))
    b = complex(b.replace(' ', ''))
    if move == '+':
        res = a + b
    elif move == '-':
        res = a - b
    elif move == '*':
        res = a * b
    elif move == '/':
        res = a / b
    return res