import pytest
from dsnutter_conversion_units.View_Model.Conversion_VM import Conversion_VM
from dsnutter_conversion_units.Model.Conversion import Conversion
from dependency_injector import containers, providers
from typing import Callable

class Test_Conversion_VM:


    @pytest.mark.parametrize('fn, value, converted', 
            [
                ("x + 1", 33, 34),
                ("x * 2", 33, 66),
                ("x / 2", 8, 4),
                ("x - 2", 4, 2)
            ])
    def test_convert(self, fn: str, value: float, converted: float):

        vm = Conversion_VM("temperature", {
    "temperature":
    {
            "ThinkDifferent":
            {
                "Kelvin": { "eq": fn, "ID": None }
            }
    }
}, Conversion)


        conversion = vm.conversion('ThinkDifferent', 'Kelvin')
        result = vm.convert(value, 'ThinkDifferent', 'Kelvin')

        assert result == converted

    def test_convert_invalid_equation(self):
        with pytest.raises(ValueError) as resultError:
        
            fn = "x * y + 1"

            vm = Conversion_VM("temperature", {
        "temperature":
        {
                "ThinkDifferent":
                {
                    "Kelvin": { "eq": fn, "ID": None }
                }
        }
    }, Conversion)

            conversion = vm.conversion('ThinkDifferent', 'Kelvin')
            result = vm.convert(32, 'ThinkDifferent', 'Kelvin')

        assert resultError.match("Conversion function is not valid")

    def test_convert_invalid_equation_extreme(self):
        with pytest.raises(ValueError) as resultError:
        
            # could be dangerous in terms of security since we are using eval()?
            fn = "input()"

            vm = Conversion_VM("temperature", {
        "temperature":
        {
                "ThinkDifferent":
                {
                    "Kelvin": { "eq": fn, "ID": None }
                }
        }
    }, Conversion)

            conversion = vm.conversion('ThinkDifferent', 'Kelvin')
            result = vm.convert(32, 'ThinkDifferent', 'Kelvin')

        assert resultError.match("Conversion function is not valid")

    def test_convert_invalid_equation_unmatched_parens(self):
        with pytest.raises(SyntaxError) as resultError:
        
            fn = "x )( 1"

            vm = Conversion_VM("temperature", {
        "temperature":
        {
                "ThinkDifferent":
                {
                    "Kelvin": { "eq": fn, "ID": None }
                }
        }
    }, Conversion)

            conversion = vm.conversion('ThinkDifferent', 'Kelvin')
            result = vm.convert(32, 'ThinkDifferent', 'Kelvin')

        # DSN Notes: does this work?
        assert resultError.match("unmatched '\\)'")
