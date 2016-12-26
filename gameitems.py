import random

MIN_KEG = 1
MAX_KEG = 90

class Bag(object):
    """A bag provides kegs"""

    def __init__(self):
        """Fill a bag with kegs"""
        self.bag = [str(i) for i in range(MIN_KEG, MAX_KEG + 1)]

    def get_keg(self):
        """Return a random keg from the bag"""
        try:
            selected_keg = random.choice(self.bag)
            self.bag.remove(selected_keg)
            return selected_keg
        except (IndexError, ValueError):
            print "Bag is empty! -> {}".format(self.bag)
            return None

class Card(object):
    """Initialize a card"""
    LINE_LEN = 9
    NUMBERS_IN_LINE = 5
    EMPTY_CELLS = LINE_LEN - NUMBERS_IN_LINE
    LINE_COUNT = 3

    def __init__(self, name):
        """Initialize a new card"""
        self.name = name
        self.pool = [str(i) for i in range(MIN_KEG, MAX_KEG + 1)]
        self.card = [self._get_line() for i in range(self.LINE_COUNT)]

    def _get_line(self):
        """Generate a line"""
        empty_indexes = self._get_empty_indexes()
        line = []
        for i in range(self.LINE_LEN):
            if i not in empty_indexes:
                line.append(' ')
            else:
                line.append(self._get_number())
        return line

    def _get_empty_indexes(self):
        """Generate random _empty_cells indexes without dublicates"""
        return random.sample(range(self.LINE_LEN), self.EMPTY_CELLS)

    def _get_number(self):
        """Return a random number from the pool or
                  'None' if the pool is empty.
        """
        try:
            selected_number = random.choice(self.pool)
            self.pool.remove(selected_number)
            return selected_number
        except (IndexError, ValueError):
            print "Pool is empty! -> {}".format(self.pool)
            return None

    def check(self, keg):
        """Return tuple: (line number of the card, keg index) or
                  'None' if keg value not found.
        """
        for i, line in enumerate(self.card):
            if keg in line:
                ikeg = line.index(keg)
                return (i, ikeg)
        return None

    def cross(self, ikeg, index):
        """Cross keg value"""
        try:
            self.card[index][ikeg] = '-'
        except (IndexError, ValueError):
            print "Can't cross a keg {} on line {}".format(ikeg, index)
            print self.card

    def check_win_condition(self):
        """Return line number if all kegs for a line is crossed otherwise
           return 0"""
        for index, line in enumerate(self.card):
            if self._check_line(line):
                return index + 1
        return 0

    def _check_line(self, line):
        """Return 1 if all kegs are crossed otherwise
            return 0"""
        for item in line:
            if item.isdigit():
                return 0
        return 1

    def __str__(self):
        """Print a card"""
        card = '-'*10 + self.name + '-'*9 + '\n'
        for line in self.card:
            card += ' '.join(['{:2}'.format(item) for item in line])
            card += '\n'
        card += '-'*26 + '\n'
        return card
