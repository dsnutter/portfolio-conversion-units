import pytest
from axion_challenge.helpers.Enums import TemperatureTypes
from axion_challenge.controller.Conversion_Controller import Conversion_Controller
from axion_challenge.model.Conversion import Conversion

class Test_Conversion_Controller:

    def test_convert(self):
        fn = lambda x: x + 1

        conv = Conversion(TemperatureTypes.Fahrenheit, { TemperatureTypes.Celsius: fn } )

        controller = Conversion_Controller(conv)
        result = controller.convert(32, TemperatureTypes.Celsius)

        assert result == 33

    def test_convert_with_custom_deinition(self):
        conv = Conversion(TemperatureTypes.Fahrenheit, {})

        fn = lambda x: x + 1
        conv.define_conversion(TemperatureTypes.Celsius, fn)

        controller = Conversion_Controller(conv)
        result = controller.convert(32, TemperatureTypes.Celsius)

        assert result == 33
