from ..helpers.Enums import GradeTypes
from .Base_Model import Base_Model

class Response(Base_Model):

    def __init__(self, answer: str, student_id: str) -> None:
        self._answer = answer   
        self._grade = GradeTypes.INCORRECT
        self._student_id = student_id

    @property
    def grade(self) -> GradeTypes:
        return self._grade

    @grade.setter
    def grade(self, value: str) -> None:
        self._grade = value

    @property
    def answer(self) -> str:
        return self._answer

    @answer.setter
    def answer(self, value: str) -> None:
        self._answer = value

    def __str__(self) -> str:
        result = 'Answer: {}\n'.format(self._answer)
        result += 'Grade: {}\n'.format(self._grade)
        return result


