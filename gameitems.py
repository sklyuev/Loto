import random

class Bag(object):
    """A bag provides kegs"""
    MIN_KEG = 1
    MAX_KEG = 90

    def __init__(self):
        """Fill a bag with kegs"""
        self.bag = [i for i in range(self.MIN_KEG, self.MAX_KEG + 1)]

    def get_keg(self):
        """Return a random keg from the bag"""
        try:
            selected_keg = random.choice(self.bag)
            self.bag.remove(selected_keg)
            return selected_keg
        except (IndexError, ValueError):
            print "Bag is empty! -> {}".format(self.bag)
            return None
