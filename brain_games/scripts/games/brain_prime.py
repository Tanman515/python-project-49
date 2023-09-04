from brain_games.engine import playing, TRIES
from random import choice
from brain_games.is_prime import is_prime
from brain_games.cli import welcome_user


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    condition = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    for attempt in range(TRIES):
        numbers = (2, 3, 5, 7, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 6, 22, 36, 15, 12, 50, 72, 74, 78) # noqa
        number = choice(numbers)
        answer = 'yes' if is_prime(number) else 'no'
        result = playing(condition, number, answer, attempt, name)
        if not result:
            break


if __name__ == '__main__':
    main()
