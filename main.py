import gameitems

def handle_response(resp):
    """Return 1 for  positive response or
              0 for negative"""
    while True:
        if resp in ["y", "yes"]:
            return 1
        elif resp in ["n", "no"]:
            return 0
        else:
            print "Input:{%s} is invalid! Try again!"
            resp = raw_input()

if __name__ == '__main__':
    bag = gameitems.Bag()
    my_card = gameitems.Card("My card")

    print my_card

    count = 1
    while True:
        keg = bag.get_keg()  # draw a new keg
        if keg:
            print "New number: {}".format(keg)
            check_result = my_card.check(keg)
            if check_result:
                line_index, keg_index = check_result
                print "Do you want to cross the number {} on line {}.\n" \
                      "(y/n)?".format(keg, line_index + 1)
                response = raw_input().lower()
                if handle_response(response):
                    my_card.cross(keg_index, line_index)
                    winner_line = my_card.check_win_condition()
                    if winner_line:
                        print "!!!  " + "WIN" + " !!!"
                        print "All kegs are corssed on line: \
                              {}".format(winner_line)
                        print my_card
                        print "Game duration: {} turns".format(count)
                        break
                    print my_card
            count += 1
        else:
            # Bag is empty
            print 'Game over!'
            break
