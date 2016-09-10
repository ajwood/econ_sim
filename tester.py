#!/usr/bin/python

from econ_sim.Simulation import Simulation
from econ_sim.Resources import Brick, Wool, Ore

def example1():
    sim = Simulation()
    b = Brick(sim)

    # Show depreciation
    for _ in range(10):
        print "{} o'clock -- My {} is worth {}".format(sim.now, b, b.value)
        sim.ticktock()


def example2():
    sim = Simulation()

    def print_net_worth(bnk):
        total = 0
        for res, supply in bnk.iteritems():
            subtotal = sum( [x.value for x in supply] )
            total += subtotal
            print "{}:\t {}".format(res, subtotal)
        print '--------------'
        print 'total:\t {}\n'.format(total)

    # Show a collection of resources. Could create a class for this, to manage
    # acquisition, access and spending of your resources
    bank = { r: [] for r in ('brick', 'wool', 'ore')}

    bank['brick'].append(Brick(sim))
    bank['brick'].append(Brick(sim))
    bank['wool'].append(Wool(sim))

    print_net_worth(bank)
    sim.ticktock()
    print '========'

    bank['brick'].append(Brick(sim))
    bank['wool'].append(Wool(sim))
    bank['ore'].append(Ore(sim))

    print_net_worth(bank)
    sim.ticktock()

    bank['brick'].append(Brick(sim))
    bank['brick'].append(Brick(sim))
    bank['ore'].append(Ore(sim))


    # Watch our wool go bad! Guess it costs to dispose of. Its depreciation
    # function should really hit a floor
    for _ in range(10):
        sim.ticktock(20)
        print_net_worth(bank)



if __name__ == '__main__':
    example1()

    print "\n========\n"

    example2()


