from ..model import Conversion

class Conversion_Controller:

    _result = 0.0

    def __init__(self, conversion):
        self._conversion = conversion

    def convert(self, input, toType):
        fn = self._conversion.get_fn(toType)
        self._result = fn(input)

        return self._result
    
    def get_result(self):
        return self._result
