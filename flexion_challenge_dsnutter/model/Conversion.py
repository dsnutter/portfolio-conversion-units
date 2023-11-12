from .Base_Model import Base_Model


class Conversion(Base_Model):

    def __init__(self, from_type: str, to_type: str, equation: str) -> None:
        self._from_type = from_type
        self._to_type = to_type
        if Conversion.is_equation_valid(equation):
            self._equation = equation
            temp = "lambda x: {}".format(self._equation)
            self._equation_lambda = eval(temp)
        else:
            raise ValueError("Conversion function is not valid")

    @property
    def from_type(self) -> str:
        return self._from_type

    @property
    def to_type(self) -> str:
        return self._to_type

    @property
    def equation_lambda(self):
         return self._equation_lambda

    # this is for security as we are using eval(), we need to sanitize the input for it
    #   in terms of what was passed in since people could shell out to host os and delete a file if we did not
    @staticmethod
    def is_equation_valid(input: str):
        sanitized = True
        # if not digits or parens or number operations. x is only possible variable
        for x in input:
            if not (x.isdigit() or x in ('(', ')', '+', '-', '-', '*', ' ', 'x')):
                sanitized = False
                break
        # if no matching parens
        if input.count('(') != input.count(')'):
            sanitized = False
        return sanitized

    def __str__(self) -> str:
        result = 'From Type: {}\n'.format(self._from_type)
        result += 'To Type: {}\n'.format(self._to_type)
        result += '\tEquation: {}\n'.format(str(self._fn))
        return result

