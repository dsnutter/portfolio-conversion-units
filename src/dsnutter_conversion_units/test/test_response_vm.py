import pytest
from ..helpers.Enums import GradeTypes, BackendTypes, BasicTypes
from ..View_Model.Response_VM import Response_VM
from ..Model.Response import Response
from ..Data.Data_Responses_CSV import Data_Responses_CSV
from ..di.Configurations import Configurations

class Test_Response_VM:

    @pytest.mark.parametrize('response, answer, grade, to_type, from_type', 
        [
            ("1", 0, GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
            ("1.2", 1.2, GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
            ("1.2", 1.1, GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
            # rounded
            ("1.256", 1.278, GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
            ("1.256", 1.1222, GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
            # negative
            ("-1.2", -1.2, GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
            ("-1.2", -1.1, GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
            # rounded negative
            ("-1.256", -1.278, GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
            ("-1.256", -1.1222, GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
            # invalid
            ("1.2", 1.2, GradeTypes.INVALID, 'dog', 'Farenheit'),
            ("1.2", 1.2, GradeTypes.INVALID, 'Celsius', 'dog')
        ])
    def test_grade(self, response, answer, grade, to_type, from_type):

        config = Configurations(BackendTypes.JSON, '', '')

        config.conversions_config = { 
    "temperature":
    {
            "Farenheit":
            {
                "Celsius": { "eq": "x + 1", "ID": None }
            }
    }}
        config.responses_config =                         {
    "temperature": {
        "ABC123": [
            {
                "response": response,
                "answer": answer,
                "from_type": from_type,
                "to_type": to_type,
                "grade": grade,
                "timestamp": "2023-10-01 04:00 PM",
                "ID": ''
            }
        ]}}


        c = Response_VM('temperature', BackendTypes.JSON, config, Response, Data_Responses_CSV(BasicTypes.Response, "temp.csv" ))

        c.add('ABC123', {
                "response": response,
                "answer": answer,
                "from_type": from_type,
                "to_type": to_type,
                "grade": grade,
                "timestamp": "2023-10-01 04:00 PM",
                "ID": ''
        })
        conv = Conversion_VM('temperature', BackendTypes.JSON, config, Conversion)
        c._convert_input = conv.convert_input_as_static
        result = c.get_response(from_type, to_type, 'ABC123', '2023-10-01 04:00 PM')[0]
        assert result.grade == grade

