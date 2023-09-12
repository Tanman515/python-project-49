#!/usr/bin/env python3


from brain_games.engine import playing, TRIES
from random import randint
from brain_games.cli import welcome_user


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    condition = 'Answer "yes" if the number is even, otherwise answer "no".'
    for attempt in range(TRIES):
        number = randint(1, 100)
        answer = 'yes' if number % 2 == 0 else 'no'
        result = playing(condition, number, answer, attempt, name)
        if not result:
            break


if __name__ == '__main__':
    main()
