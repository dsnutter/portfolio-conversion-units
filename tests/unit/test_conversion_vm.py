import pytest
from flexion_challenge_dsnutter.View_Model.Conversion_VM import Conversion_VM
from flexion_challenge_dsnutter.Model.Conversion import Conversion
from flexion_challenge_dsnutter.helpers.Enums import BackendTypes
from flexion_challenge_dsnutter.di.Configurations import Configurations

class Test_Conversion_VM:


    @pytest.mark.parametrize('fn, value, converted', 
            [
                ("x + 1", 33, 34),
                ("x * 2", 33, 66),
                ("x / 2", 8, 4),
                ("x - 2", 4, 2)
            ])
    def test_convert(self, fn: str, value: float, converted: float):

        config = Configurations(BackendTypes.JSON, '', '')

        config.conversions_config = {
    "temperature":
    {
            "ThinkDifferent":
            {
                "Kelvin": { "eq": fn, "ID": None }
            }
    }
}
        config.responses_config = {
    "temperature": {
        "ABC123": [
            {
                "response": "",
                "answer": "",
                "from_type": '',
                "to_type": '',
                "grade": '',
                "timestamp": "2023-10-01 04:00 PM",
                "ID": ''
            }
        ]}}

        vm = Conversion_VM("temperature", BackendTypes.JSON, config, Conversion)

        conversion = vm.conversion('ThinkDifferent', 'Kelvin')
        result = vm.convert_input(value, 'ThinkDifferent', 'Kelvin')

        assert result == converted

    def test_convert_invalid_equation(self):
        with pytest.raises(ValueError) as resultError:
        
            fn = "x * y + 1"

            config = Configurations(BackendTypes.JSON, '', '')

            config.conversions_config = {
        "temperature":
        {
                "ThinkDifferent":
                {
                    "Kelvin": { "eq": fn, "ID": None }
                }
        }
    }
            config.responses_config = {
        "temperature": {
            "ABC123": [
                {
                    "response": "",
                    "answer": "",
                    "from_type": '',
                    "to_type": '',
                    "grade": '',
                    "timestamp": "2023-10-01 04:00 PM",
                    "ID": ''
                }
    ]}}

            vm = Conversion_VM("temperature", BackendTypes.JSON, config, Conversion)

            conversion = vm.conversion('ThinkDifferent', 'Kelvin')
            result = vm.convert_input(32, 'ThinkDifferent', 'Kelvin')

        assert resultError.match("Conversion function is not valid")

    def test_convert_invalid_equation_extreme(self):
        with pytest.raises(ValueError) as resultError:
        
            # could be dangerous in terms of security since we are using eval()?
            fn = "input()"

            config = Configurations(BackendTypes.JSON, '', '')

            config.conversions_config = {
        "temperature":
        {
                "ThinkDifferent":
                {
                    "Kelvin": { "eq": fn, "ID": None }
                }
        }
    }
            config.responses_config = {
        "temperature": {
            "ABC123": [
                {
                    "response": "",
                    "answer": "",
                    "from_type": '',
                    "to_type": '',
                    "grade": '',
                    "timestamp": "2023-10-01 04:00 PM",
                    "ID": ''
                }
    ]}}


            vm = Conversion_VM("temperature", BackendTypes.JSON, config, Conversion)

            conversion = vm.conversion('ThinkDifferent', 'Kelvin')
            result = vm.convert_input(32, 'ThinkDifferent', 'Kelvin')

        assert resultError.match("Conversion function is not valid")

    def test_convert_invalid_equation_unmatched_parens(self):
        with pytest.raises(SyntaxError) as resultError:
        
            fn = "x )( 1"

            config = Configurations(BackendTypes.JSON, '', '')

            config.conversions_config = {
        "temperature":
        {
                "ThinkDifferent":
                {
                    "Kelvin": { "eq": fn, "ID": None }
                }
        }
    }
            config.responses_config = {
        "temperature": {
            "ABC123": [
                {
                    "response": "",
                    "answer": "",
                    "from_type": '',
                    "to_type": '',
                    "grade": '',
                    "timestamp": "2023-10-01 04:00 PM",
                    "ID": ''
                }
    ]}}


            vm = Conversion_VM("temperature", BackendTypes.JSON, config, Conversion)

            conversion = vm.conversion('ThinkDifferent', 'Kelvin')
            result = vm.convert_input(32, 'ThinkDifferent', 'Kelvin')

        # DSN Notes: does this work?
        assert resultError.match("unmatched '\\)'")
