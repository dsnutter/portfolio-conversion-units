import pytest

from flexion_challenge.helpers import Enums
from flexion_challenge.controller.Response_Controller import Response_Controller
from flexion_challenge.model.Response import Response

class Test_Response_Controller:

    def test_invalid(self):

        resp = Response('a')
        c = Response_Controller(resp)

        c.grade(0)
        result = resp.get_grade()
        assert result == Enums.GradeTypes.INVALID

    def test_correct(self):

        resp = Response('1.2')
        c = Response_Controller(resp)

        c.grade(1.2)
        result = resp.get_grade()
        assert result == Enums.GradeTypes.CORRECT

    def test_incorrect(self):

        resp = Response('1.2')
        c = Response_Controller(resp)

        c.grade(1.1)

        result = resp.get_grade()
        assert result == Enums.GradeTypes.INCORRECT

    def test_correct_rounded(self):

        resp = Response('1.256')
        c = Response_Controller(resp)

        c.grade(1.278)
        result = resp.get_grade()
        assert result == Enums.GradeTypes.CORRECT

    def test_incorrect_rounded(self):

        resp = Response('1.256')
        c = Response_Controller(resp)

        c.grade(1.1222)

        result = resp.get_grade()
        assert result == Enums.GradeTypes.INCORRECT

    def test_correct_negative(self):

        resp = Response('-1.2')
        c = Response_Controller(resp)

        c.grade(-1.2)
        result = resp.get_grade()
        assert result == Enums.GradeTypes.CORRECT

    def test_incorrect_negative(self):

        resp = Response('-1.2')
        c = Response_Controller(resp)

        c.grade(-1.1)

        result = resp.get_grade()
        assert result == Enums.GradeTypes.INCORRECT

    def test_correct_rounded_negative(self):

        resp = Response('-1.256')
        c = Response_Controller(resp)

        c.grade(-1.278)
        result = resp.get_grade()
        assert result == Enums.GradeTypes.CORRECT

    def test_incorrect_rounded_negative(self):

        resp = Response('-1.256')
        c = Response_Controller(resp)

        c.grade(-1.1222)

        result = resp.get_grade()
        assert result == Enums.GradeTypes.INCORRECT
