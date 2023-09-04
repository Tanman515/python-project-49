from brain_games.engine import playing, TRIES
from random import randint
import math
from brain_games.cli import welcome_user


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    condition = 'Find the greatest common divisor of given numbers.'
    for attempt in range(TRIES):
        number1 = randint(1, 100)
        number2 = randint(1, 100)
        numbers = f'{number1} {number2}'
        answer = str(math.gcd(number1, number2))
        result = playing(condition, numbers, answer, attempt, name)
        if not result:
            break


if __name__ == '__main__':
    main()
