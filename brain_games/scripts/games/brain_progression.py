from brain_games.engine import playing, TRIES
from brain_games.maker_progression import make_progression
from brain_games.maker_progression import encode_progression_and_get_hide_num
from brain_games.cli import welcome_user


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    condition = 'What number is missing in the progression?'
    for attempt in range(TRIES):
        progression = make_progression()
        progression, answer = encode_progression_and_get_hide_num(progression)
        result = playing(condition, progression, answer, attempt, name)
        if not result:
            break


if __name__ == '__main__':
    main()
