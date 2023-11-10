from ..helpers.Enums import GradeTypes
from ..model import Response

class Response_Controller:

    def __init__(self, response):
        self._response = response

    def grade(self, calculatedAnswer = 0.0):                
        try:
            if round(float(self._response.get_answer()), 1) == round(calculatedAnswer, 1):
                self._response.set_grade(GradeTypes.CORRECT)
        except ValueError:
            self._response.set_grade(GradeTypes.INVALID)
