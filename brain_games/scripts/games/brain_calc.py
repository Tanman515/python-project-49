from brain_games.engine import playing
from random import randint, choice


def main():
	condition = 'What is the result of the expression?'
	expressions = []
	for _ in range(3):
		number1 = randint(1, 100)
		number2 = randint(1, 100)
		symbol = choice(('+', '-', '*'))
		expressions.append(f'{number1} {symbol} {number2}')
	answers = [str(eval(expr)) for expr in expressions]
	playing(condition, expressions, answers)


if __name__ == '__main__':
	main()