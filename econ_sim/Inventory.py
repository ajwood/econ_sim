
import sys
import matplotlib.pyplot as plt

import numpy as np

class Inventory(object):
    def __init__(self):
        self.inventory = dict()

        # TODO do proper timestamps with the simulator clock, and represent in
        # a pandas dataframe
        self.balance_history = {'Total': []}



    def deposit(self, *resources):
        for r in resources:
            key = type(r).__name__
            try:
                l = self.inventory[key]
            except KeyError:
                self.inventory[key] = []
                l = self.inventory[key]
            l.append(r)
        #self.update_balance()

    # TODO need control over which to withdraw, since they're age-dependent. Right now we're FIFO
    def withdraw(self, spec):
        for res, n in spec.iteritems():
            try:
                l = self.inventory[res]
            except KeyError:
                raise Exception("TODO: handle asking for a resource that we've never seen")

            # TODO should we complain about depleting?
            if len(l) < n:
                n = len(l)
            ret = [ l.pop(0) for _ in range(n) ]

        #self.update_balance()
        return ret
        
    def print_net_worth(self):
        total = 0
        for res, supply in self.inventory.iteritems():
            subtotal = sum( [x.value for x in supply] )
            total += subtotal
            print "{}:\t {}".format(res, subtotal)
        print '--------------'
        print 'total:\t {}\n'.format(total)

    def plot_balance_history(self):
        for res, history in self.balance_history.iteritems():
            plt.plot(history, label=res)
        plt.legend(loc='upper left')
        plt.show()

    # Would be nice to have this happen automatically at deposit/withdraw, however I'd want to be able to do both a withdraw and deposit in the same transaction
    def update_balance(self):
        total = 0
        for res, supply in self.inventory.iteritems():
            try:
                l = self.balance_history[res]
            except KeyError:
                self.balance_history[res] = [ 0 for _ in self.balance_history['Total'] ]
                l = self.balance_history[res]
            subtotal = sum( [x.value for x in supply] )
            l.append(subtotal)
            total += subtotal
        self.balance_history['Total'].append(total)
