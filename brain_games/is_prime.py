def is_prime(number):
    if number < 2:
        return False
    else:
        for i in range(2, number//2):
            if number % i == 0:
                return False
        return True
