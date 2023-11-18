import pytest
from ..helpers.functions import Functions

class Test_Helpers:
    @pytest.mark.parametrize('eq, result', 
            [
                ("x + 1", True),
                ("x * 2", True),
                ("x / 2", True),
                ("x - 2", True),
                ("(x - 2) * 2", True),
                ("x + 2.1", True),
                ("x", True),
                ("(x + 1)", True),
                ("(x + 1))", False),
                ("input()", False),
                ("+a+", False)
            ])
    def test_convert(self, eq, result):
        temp = Functions.does_equation_pass_whitelist(eq)

        assert temp == result

    @pytest.mark.parametrize('value, places, result',
            [
                ('3.14159', 2, '3.14'),
                ('3.145', 2, '3.15'),
                ('3.56', 1, '3.6'),
                ('3.88', 1, '3.9'),
                ('3.24', 1, '3.2'),
                ('0.0', 2, '0.0'),
                ('-3.14159', 2, '-3.14'),
                ('-3.14559', 2, '-3.15'),
            ])
    def test_round_float_decimal_places(self, value, places, result):

        temp = Functions.round_float_decimal_places(value, places)

        assert temp == result