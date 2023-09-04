from brain_games.engine import playing, TRIES
from random import randint, choice
from brain_games.cli import welcome_user


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    condition = 'What is the result of the expression?'
    for attempt in range(TRIES):
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
        result = playing(condition, expression, answer, attempt, name)
        if not result:
            break


if __name__ == '__main__':
    main()
