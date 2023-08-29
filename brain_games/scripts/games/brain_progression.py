from random import randint
from brain_games.engine import playing


def main():
	condition = 'What number is missing in the progression?'
	progressions = []
	results = []
	questions = []
	for _ in range(3):
		start = randint(1, 20)
		step = randint(1, 10)
		length = randint(5, 10)
		string = ''
		for i in range(length):
			string += f'{str(start + step*i)} '
		progressions.append(string.strip())
	for progression in progressions:
		numbers = progression.split()
		index_hide_number = randint(1, len(numbers) - 1)
		results.append(numbers.pop(index_hide_number))
		numbers.insert(index_hide_number, '..')
		questions.append(' '.join(numbers))
	playing(condition, questions, results)


if __name__ == '__main__':
	main()