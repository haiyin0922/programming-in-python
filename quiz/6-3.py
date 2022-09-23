class Temperature:
    def __init__(self, degree, unit='C'):
        if not type(degree) in {int, float}:
            raise TypeError('degree must be int or float')
        if not unit in {'C', 'F'}:
            raise ValueError("unit must be 'C' or 'F'")
        self._degree = degree
        self._unit = unit
    def __repr__(self):
        return self.__class__.__name__ + f"({self._degree:.1f}, '{self._unit}')"
    def get_temp(self, unit):
        if self._unit == 'F' and unit == 'C': # F to C
            return ((self._degree - 32) * 5 / 9, unit)
        elif self._unit == 'C' and unit == 'F': # C to F
            return ((self._degree * 9 / 5) + 32, unit)
        else:
            return (self._degree, unit)

# Your code here to define the NewTemp class subclassing Temperature
# with __add__ and __sub__ methods
class NewTemp(Temperature):
    def __add__(self, RHS):
        x = NewTemp(self._degree, self._unit)
        if type(RHS) == int or type(RHS) == float:
            x._degree += RHS
        else:
            x._degree += RHS.get_temp(self._unit)[0]
        return x
    def __sub__(self, RHS):
        x = NewTemp(self._degree, self._unit)
        if type(RHS) == int or type(RHS) == float:
            x._degree -= RHS
        else:
            x._degree -= RHS.get_temp(self._unit)[0]
        return x

# For judging purpose
for i in range(4):
    instantiation_statement = input()
    exec(instantiation_statement)
for i in range(4):
    test_code = input()
    exec(test_code)