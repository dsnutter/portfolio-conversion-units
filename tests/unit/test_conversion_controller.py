import pytest
from dsnutter_conversion_units.controller.Conversion_Controller import Conversion_Controller
from dsnutter_conversion_units.model.Conversion import Conversion

class Test_Conversion_Controller:

    def test_convert(self):
        fn = lambda x: x + 1

        conv = Conversion('Fahrenheit', 'Celsius', fn )

        controller = Conversion_Controller(conv)
        result = controller.convert(32, 'Celsius')

        assert result == 33

    def test_convert_with_custom_deinition(self):
        conv = Conversion('Fahrenheit', 'Celsius', (lambda x: x + 2))

        fn = lambda x: x + 1
        conv.set_fn(fn)

        controller = Conversion_Controller(conv)
        result = controller.convert(32, 'Celsius')

        assert result == 33
