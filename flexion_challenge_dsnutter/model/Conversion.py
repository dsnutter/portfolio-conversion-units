from .Base_Model import Base_Model
from ..helpers.functions import Functions

class Conversion(Base_Model):

    def __init__(self, from_type: str, to_type: str, equation: str) -> None:
        self._from_type = from_type
        self._to_type = to_type
        self._equation = equation
        self._equation_lambda = Conversion.get_lambda(equation)

    @staticmethod
    def get_lambda(equation):
        if Functions.does_equation_pass_whitelist(equation):
            temp = "lambda x: {}".format(equation)
            equation_lambda = eval(temp)
        else:
            raise ValueError("Conversion function is not valid")
        return equation_lambda

    @property
    def from_type(self) -> str:
        return self._from_type

    @property
    def to_type(self) -> str:
        return self._to_type

    @property
    def equation(self):
         return self._equation

    # @equation.setter
    # def equation(self, value):
    #      self._equation = value
    #      self._equation_lambda = Conversion.get_lambda(value)

    @property
    def equation_lambda(self):
         return self._equation_lambda

    def __str__(self) -> str:
        result = 'From Type: {}\n'.format(self._from_type)
        result += 'To Type: {}\n'.format(self._to_type)
        result += '\tEquation: {}\n'.format(str(self._fn))
        return result

