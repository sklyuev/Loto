import random
import gameitems

if __name__ == '__main__':
    bag = gameitems.Bag()
    my_card = gameitems.Card("My card")
    pc_card = gameitems.Card("PC card")

    print my_card
    print pc_card
    
    while True:
        keg = bag.get_keg()
        if keg:
            print "New number: {}".format(keg)
        else:
            print 'Game over!'
            break
