
import sys
import matplotlib.pyplot as plt

import numpy as np

class Inventory(object):
    def __init__(self):
        self.inventory = dict()
        self.balance_history = {'total': []}



    def deposit(self, r):
        key = type(r).__name__
        try:
            l = self.inventory[key]
        except KeyError:
            self.inventory[key] = []
            l = self.inventory[key]
        l.append(r)
        self.update_balance()

    # TODO need control over which to withdraw, since they're age-dependent. Right now we're FIFO
    def withdraw(self, type_, n=1):
        try:
            l = self.inventory[type_]
        except KeyError:
            raise Exception("TODO: handle asking for a resource that we've never seen")

        ret = [ l.pop(0) for _ in range(n) ]
        self.update_balance()
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

    def update_balance(self):
        total = 0
        for res, supply in self.inventory.iteritems():
            try:
                l = self.balance_history[res]
            except KeyError:
                self.balance_history[res] = [ 0 for _ in self.balance_history['total'] ]
                l = self.balance_history[res]
            subtotal = sum( [x.value for x in supply] )
            l.append(subtotal)
            total += subtotal
        self.balance_history['total'].append(total)
