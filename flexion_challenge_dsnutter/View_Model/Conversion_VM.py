from ..Model import Conversion
from .Base_VM import Base_VM

# controls operationss on the conversion Models, and persistance
class Conversion_VM(Base_VM):

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
