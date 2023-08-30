from random import randint


def make_progressions(length):
    progressions = []
    for _ in range(length):
        start = randint(1, 20)
        step = randint(1, 10)
        length = randint(5, 10)
        string = ''
        for i in range(length):
            string += f'{str(start + step*i)} '
        progressions.append(string.strip())
    return progressions
