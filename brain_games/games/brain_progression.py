from random import randint


def make_progression():
    first_number = randint(1, 20)
    step_between_numbers = randint(1, 10)
    length = randint(5, 10)
    progression = ''
    for i in range(length):
        progression += f'{str(first_number + step_between_numbers*i)} '
    return progression.strip()


def encode_progression_and_get_hide_num(progression):
    numbers = progression.split()
    index_hide_number = randint(0, len(numbers) - 1)
    number = numbers.pop(index_hide_number)
    numbers.insert(index_hide_number, '..')
    progression = ' '.join(numbers)
    return progression, number


def progression():
    condition = 'What number is missing in the progression?'
    progression = make_progression()
    progression, answer = encode_progression_and_get_hide_num(progression)
    return condition, progression, answer
