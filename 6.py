def arithmetic_operation(symb):
    if symb == '+':
        return lambda a, b: a + b
    if symb == '-':
        return lambda a, b: a - b
    if symb == '*':
        return lambda a, b: a * b
    if symb == '/':
        return lambda a, b: a / b


operation = arithmetic_operation('+')
print(operation(1, 4))

operation = arithmetic_operation('-')
print(operation(5, 2))

operation = arithmetic_operation('*')
print(operation(3, 4))

operation = arithmetic_operation('/')
print(operation(8, 2))