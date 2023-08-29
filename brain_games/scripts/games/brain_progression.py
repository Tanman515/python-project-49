from random import randint
from brain_games.engine import playing
from brain_games.maker_progressions import make_progressions


def main():
	condition = 'What number is missing in the progression?'
	results = []
	questions = []
	progressions = make_progressions(length=3)
	for progression in progressions:
		numbers = progression.split()
		index_hide_number = randint(1, len(numbers) - 1)
		results.append(numbers.pop(index_hide_number))
		numbers.insert(index_hide_number, '..')
		questions.append(' '.join(numbers))
	playing(condition, questions, results)


if __name__ == '__main__':
	main()