from ..model import Conversion
from .Base_Controller import Base_Controller

# controls operationss on the conversion models, and persistance
class Conversion_Controller(Base_Controller):

    def __init__(self, conversion: Conversion.Conversion) -> None:
        self._conversion = conversion

    def convert(self, input: float) -> float:
        try:
            self._result = self._conversion.equation_lambda(input)
        except:
            raise ValueError("Cannot execute lambda function defined")

        return self._result

    def __str__(self) -> str:
        result = 'Conversion Controller: {}\n'.format(self._conversion)
        return result
