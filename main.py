import random

MIN_NUMBER = 1
MAX_NUMBER = 5


def get_number():
    numbers = random.sample(MIN_NUMBER, MAX_NUMBER)
    seen = []
    for number in numbers:
        if number not in seen:
            seen.append(number)
            yield number

if __name__ == '__main__':
    number_generator = get_number()
    while True:
        print "New number: {}".format(number_generator.next())
