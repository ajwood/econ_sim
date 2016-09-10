
class Resource(object):
    def __init__(self, sim, value, shelf_life, depreciation_func=None):
        """Resource base class (this should probably be enforced as abstract)

        Args:
            sim: a simulation object, which controls stuff like time-based behaviour
            value: the base value of one unit, in centralized currency (my mind boggles at the thought modeling context-dependent value). This will be augmented with the depreciation_func
            shelf_life: how long it takes to fully depreciate
            depreciation_func: function of age, added to value; should return a negative value for depreciation, and a positive value for appreciation. By default, value is unaffected by age.
        """
        self.sim        = sim
        self.shelf_life = shelf_life
        self.born       = sim.now
        self.base_value = value

        if depreciation_func == None:
            self.depreciation_func = lambda x: x
        else:
            self.depreciation_func = depreciation_func

    @property
    def age(self):
        return self.sim.now - self.born

    @property
    def value(self):
        return max( 0, self.base_value + self.depreciation_func( self.age ) * 20)

    def __str__(self):
        return type(self).__name__.lower()
    def __repr__(self): # FIXME remove
        return type(self).__name__.lower()


## - Not sure whether it actually makes sense to make these derived classes;
# they're just configuration values. Derived classes are only really needed if is
# distinct functions and/or behaviour. 
## - I don't like at all how the simulation object is handled
## - Note the depreciation can be more complex (e.g. piecewise, non-linear...)
class Brick(Resource):
    def __init__(self, sim):
        super(Brick, self).__init__(sim, 75, 15, 
                lambda age: -0.1 * age)

class Wood(Resource):
    def __init__(self, sim):
        super(Wood, self).__init__(sim, 100, 10,
                lambda age: -0.4 * age)

class Wool(Resource):
    def __init__(self, sim):
        super(Wool, self).__init__(sim, 125, 5,
                lambda age: -0.8 * age)

class Ore(Resource):
    def __init__(self, sim):
        super(Ore, self).__init__(sim, 150, 25,
                lambda age: -0.05 * age)


