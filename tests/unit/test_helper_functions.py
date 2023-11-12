import pytest
from dsnutter_conversion_units.helpers.functions import Functions

class Test_Helper_Functions:
    @pytest.mark.parametrize('eq, result', 
            [
                ("x + 1", True),
                ("x * 2", True),
                ("x / 2", True),
                ("x - 2", True),
                ("(x - 2) * 2", True),
                ("x", True),
                ("(x + 1)", True),
                ("(x + 1))", False),
                ("input()", False),
                ("+a+", False)
            ])
    def test_convert(self, eq, result):
        temp = Functions.is_equation_valid(eq)

        assert temp == result