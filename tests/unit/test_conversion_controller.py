import pytest
from flexion_challenge_dsnutter.controller.Conversion_Controller import Conversion_Controller
from flexion_challenge_dsnutter.model.Conversion import Conversion

class Test_Conversion_Controller:

    def test_convert(self):
        fn = "x + 1"

        conv = Conversion('Fahrenheit', 'Celsius', fn )

        controller = Conversion_Controller(conv)
        result = controller.convert(32)

        assert result == 33

    def test_convert_invalid_equation(self):
        with pytest.raises(ValueError) as resultError:
        
            fn = "x * y + 1"

            conv = Conversion('Fahrenheit', 'Celsius', fn )

            controller = Conversion_Controller(conv)
            result = controller.convert(32)

        assert resultError.match("Conversion function is not valid")

    def test_convert_invalid_equation_extreme(self):
        with pytest.raises(ValueError) as resultError:
        
            # could be dangerous in terms of security since we are using eval()?
            fn = "input()"

            conv = Conversion('Fahrenheit', 'Celsius', fn )

            controller = Conversion_Controller(conv)
            result = controller.convert(32)

        assert resultError.match("Conversion function is not valid")

    def test_convert_invalid_equation_unmatched_parens(self):
        with pytest.raises(SyntaxError) as resultError:
        
            fn = "x )( 1"

            conv = Conversion('Fahrenheit', 'Celsius', fn )

            controller = Conversion_Controller(conv)
            result = controller.convert(32)

        assert resultError.match("unmatched '\)'")
