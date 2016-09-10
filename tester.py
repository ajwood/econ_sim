#!/usr/bin/python

import sys
import random

from econ_sim.Simulation import Simulation
from econ_sim.Resources import Brick, Wool, Ore, Wood
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

def example3():
    sim = Simulation()
    inv = Inventory()

    for n in range(10000):
        n_in  = random.randint(0, 15)
        n_out = random.randint(0, 15)

        # Acquire new resources
        resources = [ Brick, Wool, Ore, Wood ]
        for _ in range(n_in):
            res = random.choice(resources)
            inv.deposit( res(sim) )

        # Ditch some old resources
        resources = inv.inventory.keys()
        if len(resources) > 0:
            withdraw = { r: 0 for r in resources }
            for _ in range(n_out):
                res = random.choice(resources)
                withdraw[res] += 1
            inv.withdraw(withdraw)

        inv.update_balance()
        sim.ticktock()

    inv.plot_balance_history()


if __name__ == '__main__':
    #example1()

    #example2()

    example3()

