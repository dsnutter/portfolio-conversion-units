from ..model import Conversion

# controls operationss on the conversion models, and persistance
class Conversion_Controller:

    _result = 0.0

    def __init__(self, conversion):
        self._conversion = conversion

    def convert(self, input, to_type):
        fn = self._conversion.get_fn(to_type)
        self._result = fn(input)

        return self._result
    
    def get_result(self):
        return self._result
