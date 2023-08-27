from random import randint


def game(name):
	print('Answer "yes" if the number is even, otherwise answer "no".')
	counter = 0
	while counter < 3:
		number = randint(1, 100)
		answer = 'yes' if number % 2 == 0 else 'no'
		print(f'Question: {number}')
		user_answer = input('Your answer: ')
		if user_answer == answer and counter < 2:
			counter += 1
			print('Correct!')
			continue
		elif user_answer == answer and counter == 2:
			counter += 1
			print('Correct!')
			print(f'Congratulations, {name}!')
			continue
		else:
			print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.")
			print(f"Let's try again, {name}!")
			break
