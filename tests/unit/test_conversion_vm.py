import pytest
from dsnutter_conversion_units.View_Model.Conversion_VM import Conversion_VM
from dsnutter_conversion_units.Model.Conversion import Conversion
from dsnutter_conversion_units.helpers.Enums import BackendTypes
from dsnutter_conversion_units.di.Configurations import Configurations

class Test_Conversion_VM:


    @pytest.mark.parametrize('fn, value, converted', 
            [
                ("x + 1", 33, 34),
                ("x * 2", 33, 66),
                ("x / 2", 8, 4),
                ("x - 2", 4, 2),
                #temperature,Farenheit,Celsius
                ("(x-32.0) * (5/9)", 32, 0),
                #temperature,Farenheit,Kelvin
                ("((x-32.0) * (5/9)) + 273.15", 0, 0),
                #temperature,Farenheit,Rankine
                ("x + 459.67", 0, 0),
                #temperature,Celsius,Farenheit
                ("(x * (9/5)) + 32.0", 0, 32),
                #temperature,Celsius,Kelvin
                ("x + 273.15", 0, 0),
                #temperature,Celsius,Rankine
                ("(x + 273.15) * 9/5", 0, 0),
                #temperature,Kelvin,Farenheit
                ("((x-273.15) * (9/5)) + 32.0", 0, 0),
                #temperature,Kelvin,Celsius
                ("x - 273.15", 0, 0),
                #temperature,Kelvin,Rankine
                ("x * 9/5", 0, 0),
                #temperature,Rankine,Farenheit
                ("x - 459.67", 0, 0),
                #temperature,Rankine,Celsius
                ("(x * 5/9) - 273.15", 0, 0),
                #temperature,Rankine,Kelvin
                ("x * 5/9", 0, 0),
                #temperature,ThinkDifferent,Kelvin
                ("x + 1", 0, 0),
                #volume,Liters,Tablespoons
                ("x * (67.0 + 2/3)", 0, 0),
                #volume,Liters,Cubic_inches
                ("x * 61.023744", 0, 0),
                #volume,Liters,Cups
                ("x * 4.2267528377", 0, 0),
                #volume,Liters,Cubic_feet
                ("x * 0.035315", 0, 0),
                #volume,Liters,Gallons
                ("x * 0.264172", 0, 0),
                #volume,Tablespoons,Liters
                ("x / (67.0 + 2/3)", 0, 0),
                #volume,Tablespoons,Cubic_inches
                ("x *  0.902344", 0, 0),
                #volume,Tablespoons,Cups
                ("x * (1/16)", 0, 0),
                #volume,Tablespoons,Cubic_feet
                ("x * 0.000522", 0, 0),
                #volume,Tablespoons,Gallons
                ("x * 0.003906", 0, 0),
                #volume,Cubic_inches,Liters
                ("x / 61.023744", 0, 0),
                #volume,Cubic_inches,Tablespoons
                ("x /  0.902344", 0, 0),
                #volume,Cubic_inches,Cups
                ("x * (1/16)", 0, 0),
                #volume,Cubic_inches,Cubic_feet
                ("x * 0.000579", 0, 0),
                #volume,Cubic_inches,Gallons
                ("x * 0.004329", 0, 0),
                #volume,Cups,Liters
                ("x / 4.2267528377", 0, 0),
                #volume,Cups,Tablespoons
                ("x / (1/16)", 0, 0),
                #volume,Cups,Cubic_inches
                ("x / (1/16)", 0, 0),
                #volume,Cups,Cubic_feet
                ("x * 0.008355", 0, 0),
                #volume,Cups,Gallons
                ("x * 0.0625", 0, 0),
                #volume,Cubic_feet,Liters
                ("x / 0.035315", 0, 0),
                #volume,Cubic_feet,Tablespoons
                ("x / 0.000522", 0, 0),
                #volume,Cubic_feet,Cubic_inches
                ("x / 0.000579", 0, 0),
                #volume,Cubic_feet,Cups
                ("x / 0.008355", 0, 0),
                #volume,Cubic_feet,Gallons
                ("x * 7.480519", 0, 0),
                #volume,Gallons,Liters
                ("x / 0.264172", 0, 0),
                #volume,Gallons,Tablespoons
                ("x / 0.003906", 0, 0),
                #volume,Gallons,Cubic_inches
                ("x / 0.004329", 0, 0),
                #volume,Gallons,Cups
                ("x / 0.0625", 0, 0),
                #volume,Gallons,Cubic_feet
                ("x / 7.480519", 0, 0)
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
