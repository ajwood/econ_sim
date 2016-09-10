class Simulation(object):
    """Simulation object. So far, this is just a clock"""
    def __init__(self):
        self.now = 0

    def ticktock(self, ticks=1):
        self.now += ticks
