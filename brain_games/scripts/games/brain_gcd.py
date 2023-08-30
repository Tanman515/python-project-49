from brain_games.engine import playing
from random import randint
import math


def main():
    condition = 'Find the greatest common divisor of given numbers.'
    numbers = [[randint(1, 100), randint(1, 100)] for _ in range(3)]
    results = [str(math.gcd(*numbers[i])) for i in range(3)]
    playing(condition, numbers, results)


if __name__ == '__main__':
    main()
