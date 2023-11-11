from ..helpers.Enums import GradeTypes

class Response:   
    _grade = GradeTypes.INCORRECT
    # answer is a string since it could contain invalid responses
    _answer = ''

    def __init__(self, answer):
        self._answer = answer   

    def set_grade(self, grade):
        self._grade = grade

    def get_grade(self):
        return self._grade

    def get_answer(self):
        return self._answer

