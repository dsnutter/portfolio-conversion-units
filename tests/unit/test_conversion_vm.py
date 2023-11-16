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
                ("(x-32.0) * (5/9)", 100, 37.8),
                #temperature,Farenheit,Kelvin
                ("((x-32.0) * (5/9)) + 273.15", 100.0, 310.9),
                #temperature,Farenheit,Rankine
                ("x + 459.67", 100.0, 559.7),
                #temperature,Celsius,Farenheit
                ("(x * (9/5)) + 32.0", 100.0, 212),
                #temperature,Celsius,Kelvin
                ("x + 273.15", 100.0, 373.2),
                #temperature,Celsius,Rankine
                ("(x + 273.15) * 9/5", 100.0, 671.7),
                #temperature,Kelvin,Farenheit
                ("((x-273.15) * (9/5)) + 32.0", 100.0, -279.7),
                #temperature,Kelvin,Celsius
                ("x - 273.15", 100, -173.2),
                #temperature,Kelvin,Rankine
                ("x * 9/5", 100, 180),
                #temperature,Rankine,Farenheit
                ("x - 459.67", 100, -359.7),
                #temperature,Rankine,Celsius
                ("(x * 5/9) - 273.15", 100, -217.6),
                #temperature,Rankine,Kelvin
                ("x * 5/9", 100, 55.6),
                #temperature,ThinkDifferent,Kelvin
                ("x + 1", 100, 101),
                #volume,Liters,Tablespoons
                ("x * (67.0 + 2/3)", 100, 6762.8),
                #volume,Liters,Cubic_inches
                ("x * 61.023744", 100, 6102.4),
                #volume,Liters,Cups
                ("x * 4.2267528377", 100, 422.7),
                #volume,Liters,Cubic_feet
                ("x * 0.035315", 100, 3.5),
                #volume,Liters,Gallons
                ("x * 0.264172", 100, 26.4),
                #volume,Tablespoons,Liters
                ("x / (67.0 + 2/3)", 100, 1.5),
                #volume,Tablespoons,Cubic_inches
                ("x *  0.902344", 100, 90.2),
                #volume,Tablespoons,Cups
                ("x * (1/16)", 100, 25),
                #volume,Tablespoons,Cubic_feet
                ("x * 0.000522", 100, 0.1),
                #volume,Tablespoons,Gallons
                ("x * 0.003906", 100, 0.4),
                #volume,Cubic_inches,Liters
                ("x / 61.023744", 100, 1.6),
                #volume,Cubic_inches,Tablespoons
                ("x /  0.902344", 100, 110.8),
                #volume,Cubic_inches,Cups
                ("x * (1/16)", 100, 6.9),
                #volume,Cubic_inches,Cubic_feet
                ("x * 0.000579", 100, 0.1),
                #volume,Cubic_inches,Gallons
                ("x * 0.004329", 100, 0.4),
                #volume,Cups,Liters
                ("x / 4.2267528377", 100, 23.7),
                #volume,Cups,Tablespoons
                ("x / (1/16)", 100, 1600),
                #volume,Cups,Cubic_inches
                ("x / (1/16)", 100, 1443.8),
                #volume,Cups,Cubic_feet
                ("x * 0.008355", 100, 0.8),
                #volume,Cups,Gallons
                ("x * 0.0625", 100, 6.3),
                #volume,Cubic_feet,Liters
                ("x / 0.035315", 100, 2831.7),
                #volume,Cubic_feet,Tablespoons
                ("x / 0.000522", 100, 191501),
                #volume,Cubic_feet,Cubic_inches
                ("x / 0.000579", 100, 172800),
                #volume,Cubic_feet,Cups
                ("x / 0.008355", 100, 11968.8),
                #volume,Cubic_feet,Gallons
                ("x * 7.480519", 100, 748.1),
                #volume,Gallons,Liters
                ("x / 0.264172", 100, 378.5),
                #volume,Gallons,Tablespoons
                ("x / 0.003906", 100, 25600),
                #volume,Gallons,Cubic_inches
                ("x / 0.004329", 100, 23100),
                #volume,Gallons,Cups
                ("x / 0.0625", 100, 1600),
                #volume,Gallons,Cubic_feet
                ("x / 7.480519", 100, 13.4)
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
