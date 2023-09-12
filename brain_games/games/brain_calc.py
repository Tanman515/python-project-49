from random import randint, choice


def calc():
    condition = 'What is the result of the expression?'
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    symbol = choice(('+', '-', '*'))
    if symbol == '+':
        answer = str(number1 + number2)
    elif symbol == '-':
        answer = str(number1 - number2)
    else:
        answer = str(number1 * number2)
    expression = f'{number1} {symbol} {number2}'
    return (condition, expression, answer)
