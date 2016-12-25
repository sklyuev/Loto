import random

class Card(object):
    '''Loto card class'''
    _line_len = 9
    _empty_cells = 4
    _to_be_filled_cells = _line_len - _empty_cells
    _line_count = 3
    _min_number = 1
    _max_number = 90

    def __init__(self):
        '''Initialize a card'''
        # self.avalible_numbers = random.sample(
        #                             (self._min_number, self._max_number),
        #                             self._max_number)
        self.card = [self.get_line() for i in range(self._line_count)]

    def get_empty_indexes(self):
        '''Generate random _empty_cells indexes without dublicates'''
        return random.sample(range(self._line_len), self._empty_cells)

    def get_number(self):
        try:
            return self.avalible_numbers.pop()
        except ValueError:
            print "Oops! Can't get next value from avalible_numbers list"

    def get_line(self):
        '''Generate a line'''
        empty_indexes = self.get_empty_indexes()
        line = []
        for i in range(self._line_len):
            if i not in empty_indexes:
                line.append(' ')
            else:
                line.append(self.get_number())
        return line

    def __str__(self):
        '''Print a card'''
        card = '-'*26 + '\n'
        for line in self.card:
            card += ' '.join(['{:2}'.format(item) for item in line])
            card += '\n'
        card += '-'*26 + '\n'
        return card

if __name__ == '__main__':
    # card = Card()
    # print card
    # print card.card
    pass
