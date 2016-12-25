import random
import gameitems

if __name__ == '__main__':
    bag = gameitems.Bag()
    while True:
        keg = bag.get_keg()
        if keg:
            print "New number: {}".format(keg)
        else:
            print 'Game over!'
            break
