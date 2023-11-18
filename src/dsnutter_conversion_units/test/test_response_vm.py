import pytest
from ..helpers.Enums import GradeTypes, BackendTypes, BasicTypes
from ..View_Model.Response_VM import Response_VM
from ..View_Model.Conversion_VM import Conversion_VM
from ..Model.Response import Response
from ..Model.Conversion import Conversion
from ..Data.Data_Responses_CSV import Data_Responses_CSV
from ..di.Configurations import Configurations


class Test_Response_VM:

    @pytest.mark.parametrize('input_value, response, grade, to_type, from_type',
                             [
                                 ("1", 0, GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 ("32", 0, GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
                                 ("1.2", 1.1, GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 # rounded
                                 ("1.256", -17.08, GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
                                 ("1.256", -17.077, GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
                                 ("1.256222", -17.075, GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
                                 ("1.2565", -17.076, GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
                                 ("1.256", 1.1222, GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 ("3.1499999999999999999", 3.2, GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 # negative
                                 ("-1.2", -18.44444, GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
                                 ("-1.2", -1.1, GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 # rounded negative
                                 ("-1.256", -18.4755, GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
                                 ("-1.256", -1.1222, GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 # invalid
                                 ("1.2", 1.2, GradeTypes.INVALID, 'dog', 'Farenheit'),
                                 ("1.2", 1.2, GradeTypes.INVALID, 'Celsius', 'dog')
                             ])
    def test_grade(self, input_value, response, grade, to_type, from_type):

        config = Configurations(BackendTypes.JSON, '', '')

        config.conversions_config = {
            "temperature":
            {
                "Farenheit":
                {
                    "Celsius": {"eq": "(x-32.0) * (5/9)", "ID": None}
                }
            }}
        config.responses_config = {
            "temperature": {
                "ABC123": [
                    {
                        "response": response,
                        "input_value": input_value,
                        "from_type": from_type,
                        "to_type": to_type,
                        "grade": grade,
                        "timestamp": "2023-10-01 04:00 PM",
                        "ID": ''
                    }
                ]}}

        conv = Conversion_VM('temperature', BackendTypes.JSON, config, Conversion)
        c = Response_VM('temperature', BackendTypes.JSON, config, Response,
                        Data_Responses_CSV(BasicTypes.Response, "./assist/temp.csv"))
        c._convert_input = conv.convert_input

        c.add('ABC123', {
            "response": response,
            "input_value": input_value,
            "from_type": from_type,
            "to_type": to_type,
            "timestamp": "2023-10-01 04:00 PM",
            "ID": ''
        })
        result = c.get_response(from_type, to_type, 'ABC123', '2023-10-01 04:00 PM')[0]
        assert result.grade == grade
