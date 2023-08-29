from brain_games.engine import playing
from random import choice
from brain_games.is_prime import is_prime


def main():
	condition = 'Answer "yes" if given number is prime. Otherwise answer "no".'
	numbers_to_ask = [choice((2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 6, 22, 36, 15, 12, 50, 72, 74, 78, 81, 85, 90)) for _ in range(3)]
	results = ['yes' if is_prime(i) else 'no' for i in numbers_to_ask]
	playing(condition, numbers_to_ask, results)	


if __name__ == '__main__':
	main()