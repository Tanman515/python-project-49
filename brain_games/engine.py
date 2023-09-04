# General game architecture


TRIES = 3
FIRST_TRY = 0
LAST_TRY = 2


def playing(condition, expression, answer, attempt, name):
    if attempt == FIRST_TRY:
        print(condition)
    print(f'Question: {expression}')
    user_answer = input('Your answer: ')
    if user_answer == answer:
        print('Correct!')
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'") # noqa
        print(f"Let's try again, {name}")
        return False
    if attempt == LAST_TRY:
        print(f'Congratulations, {name}')
    return True
