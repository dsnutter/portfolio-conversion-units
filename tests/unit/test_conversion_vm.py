import pytest
from flexion_challenge_dsnutter.View_Model.Conversion_VM import Conversion_VM
from flexion_challenge_dsnutter.Model.Conversion import Conversion

class Test_Conversion_VM:


    @pytest.mark.parametrize('fn, value, converted', 
            [
                ("x + 1", 33, 34),
                ("x * 2", 33, 66),
                ("x / 2", 8, 4),
                ("x - 2", 4, 2)
            ])
    def test_convert(self, fn, value, converted):
        conv = Conversion('Fahrenheit', 'Celsius', fn )

        controller = Conversion_VM(conv)
        result = controller.convert(value)

        assert result == converted

    def test_convert_invalid_equation(self):
        with pytest.raises(ValueError) as resultError:
        
            fn = "x * y + 1"

            conv = Conversion('Fahrenheit', 'Celsius', fn )

            controller = Conversion_VM(conv)
            result = controller.convert(32)

        assert resultError.match("Conversion function is not valid")

    def test_convert_invalid_equation_extreme(self):
        with pytest.raises(ValueError) as resultError:
        
            # could be dangerous in terms of security since we are using eval()?
            fn = "input()"

            conv = Conversion('Fahrenheit', 'Celsius', fn )

            controller = Conversion_VM(conv)
            result = controller.convert(32)

        assert resultError.match("Conversion function is not valid")

    def test_convert_invalid_equation_unmatched_parens(self):
        with pytest.raises(SyntaxError) as resultError:
        
            fn = "x )( 1"

            conv = Conversion('Fahrenheit', 'Celsius', fn )

            controller = Conversion_VM(conv)
            result = controller.convert(32)

        assert resultError.match("unmatched '\)'")
