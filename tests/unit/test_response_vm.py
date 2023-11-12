import pytest

from dsnutter_conversion_units.helpers import Enums
from dsnutter_conversion_units.View_Model.Response_VM import Response_VM
from dsnutter_conversion_units.Model.Response import Response

class Test_Response_VM:

    def test_invalid(self):

        resp = Response('a', '1234')
        c = Response_VM(resp)

        c.grade_answer(0)
        result = resp.grade
        assert result == Enums.GradeTypes.INVALID

    def test_correct(self):

        resp = Response('1.2', '1234')
        c = Response_VM(resp)

        c.grade_answer(1.2)
        result = resp.grade
        assert result == Enums.GradeTypes.CORRECT

    def test_incorrect(self):

        resp = Response('1.2', '1234')
        c = Response_VM(resp)

        c.grade_answer(1.1)

        result = resp.grade
        assert result == Enums.GradeTypes.INCORRECT

    def test_correct_rounded(self):

        resp = Response('1.256', '1234')
        c = Response_VM(resp)

        c.grade_answer(1.278)
        result = resp.grade
        assert result == Enums.GradeTypes.CORRECT

    def test_incorrect_rounded(self):

        resp = Response('1.256', '1234')
        c = Response_VM(resp)

        c.grade_answer(1.1222)

        result = resp.grade
        assert result == Enums.GradeTypes.INCORRECT

    def test_correct_negative(self):

        resp = Response('-1.2', '1234')
        c = Response_VM(resp)

        c.grade_answer(-1.2)
        result = resp.grade
        assert result == Enums.GradeTypes.CORRECT

    def test_incorrect_negative(self):

        resp = Response('-1.2', '1234')
        c = Response_VM(resp)

        c.grade_answer(-1.1)

        result = resp.grade
        assert result == Enums.GradeTypes.INCORRECT

    def test_correct_rounded_negative(self):

        resp = Response('-1.256', '1234')
        c = Response_VM(resp)

        c.grade_answer(-1.278)
        result = resp.grade
        assert result == Enums.GradeTypes.CORRECT

    def test_incorrect_rounded_negative(self):

        resp = Response('-1.256', '1234')
        c = Response_VM(resp)

        c.grade_answer(-1.1222)

        result = resp.grade
        assert result == Enums.GradeTypes.INCORRECT
