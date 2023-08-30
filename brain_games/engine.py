# General game architecture


from brain_games.cli import welcome_user


def playing(condition, expressions, answers):
    answer_false = 'is wrong answer ;(. Correct answer was'
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(condition)
    is_winner = True
    for expression, answer in zip(expressions, answers):
        print(f'Question: {expression}')
        user_answer = input('Your answer: ')
        if user_answer == answer:
            print('Correct!')
            continue
        else:
            print(f"'{user_answer}' {answer_false} '{answer}'.")
            print(f"Let's try again, {name}!")
            is_winner = False
            break
    if is_winner:
        print(f'Congratulations, {name}!')
