from random import choice


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number // 2):
        if number % i == 0:
            return False
    return True


def prime():
    condition = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    numbers = (2, 3, 5, 7, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 6, 22, 36, 15, 12, 50, 72, 74, 78) # noqa
    number = choice(numbers)
    answer = 'yes' if is_prime(number) else 'no'
    return condition, number, answer


