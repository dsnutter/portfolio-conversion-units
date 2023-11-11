

class Conversion:

    def __init__(self, from_type, to_type, fn):
        self._from_type = from_type
        self._to_type = to_type
        self._fn = fn

    @property
    def from_type(self):
        return self._from_type

    @property
    def fn(self):
        return self._fn

    # if want to add additional conversions manually, maybe needs removed?
    @fn.setter
    def fn(self, value):
        self._fn = value
    
    def __str__(self):
        result = 'From Type: {}\n'.format(self._from_type)
        result += 'To Type: {}\n'.format(self._to_type)
        result += '\tEquation: {}\n'.format(str(self._fn))
        return result

