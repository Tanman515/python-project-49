# General game architecture

from brain_games.cli import welcome_user


TRIES = 3
FIRST_TRY = 0
LAST_TRY = 2


def run(game_func):
    name = welcome_user()
    for attempt in range(TRIES):
        condition, expression, answer = game_func()
        if attempt == FIRST_TRY:
            print(condition)
        print(f'Question: {expression}')
        user_answer = input('Your answer: ')
        if user_answer == answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'") # noqa
            print(f"Let's try again, {name}!")
            break
        if attempt == LAST_TRY:
            print(f'Congratulations, {name}!')

