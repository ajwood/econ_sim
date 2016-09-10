#!/usr/bin/python

import sys

from econ_sim.Simulation import Simulation
from econ_sim.Resources import Brick, Wool, Ore
from econ_sim.Inventory import Inventory

import numpy as np

def example1():
    sim = Simulation()
    b = Brick(sim)

    # Show depreciation
    for _ in range(10):
        print "{} o'clock -- My {} is worth {}".format(sim.now, b, b.value)
        sim.ticktock()


def example2():
    sim = Simulation()
    inv = Inventory()

    inv.deposit(Brick(sim))
    inv.deposit(Brick(sim))
    inv.deposit(Brick(sim))
    inv.deposit(Wool(sim))

    inv.print_net_worth()
    sim.ticktock()

    inv.deposit(Brick(sim))
    inv.deposit(Wool(sim))
    inv.deposit(Ore(sim))

    inv.print_net_worth()
    sim.ticktock()

    inv.withdraw('Brick', n=3)
    inv.withdraw('Wool')

    inv.deposit(Brick(sim))
    inv.deposit(Brick(sim))
    inv.deposit(Ore(sim))

    inv.print_net_worth()
    sim.ticktock()


    for _ in range(10):
        sim.ticktock(20)
        inv.print_net_worth()

    print "============="

    inv.plot_balance_history()


if __name__ == '__main__':
    #example1()

    print "\n========\n"

    example2()


