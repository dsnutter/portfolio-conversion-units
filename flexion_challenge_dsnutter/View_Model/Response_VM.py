from ..helpers.Enums import GradeTypes
from ..Model import Response
from .Base_VM import Base_VM

# controls operations on the reponse Models, and persistance
class Response_VM(Base_VM):

    def __init__(self, response: Response.Response) -> None:
        self._response = response

    def grade_answer(self, calculated_answer: float) -> None:
        try:
            if round(float(self._response.answer), 1) == round(calculated_answer, 1):
                self._response.grade = GradeTypes.CORRECT
        except ValueError:
            self._response.grade = GradeTypes.INVALID

    def __str__(self) -> str:
        result = 'Response Controller: {}\n'.format(self._response)
        return result

