from random import randint
import math


def gcd():
    condition = 'Find the greatest common divisor of given numbers.'
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    numbers = f'{number1} {number2}'
    answer = str(math.gcd(number1, number2))
    return condition, numbers, answer
