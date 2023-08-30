#!/usr/bin/env python3


from brain_games.engine import playing
from random import randint


def main():
    condition = 'Answer "yes" if the number is even, otherwise answer "no".'
    numbers = [randint(1, 100) for _ in range(3)]
    answers = ['yes' if i % 2 == 0 else 'no' for i in numbers]
    playing(condition, numbers, answers)


if __name__ == '__main__':
    main()
