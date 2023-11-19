import pytest
from ..helpers.Enums import GradeTypes, BackendTypes, BasicTypes
from ..View_Model.Response_VM import Response_VM
from ..View_Model.Conversion_VM import Conversion_VM
from ..Model.Response import Response
from ..Model.Conversion import Conversion
from ..Data.Data_Responses_CSV import Data_Responses_CSV
from ..di.Configurations import Configurations


class Test_Response_VM:

    student_id = 'ABC123'
    timestamp = '2023-10-01 04:00 PM'

    def setup_method(self):
        config = Configurations(BackendTypes.JSON, '', '')

        config.conversions_config = {
            "temperature":
            {
                "Farenheit":
                {
                    "Celsius": {"eq": "(x-32.0) * (5/9)", "ID": None}
                }
            }}
        config.responses_config = {}

        conv = Conversion_VM('temperature', BackendTypes.JSON, config, Conversion)
        resp = Response_VM('temperature', BackendTypes.JSON, config, Response,
                        Data_Responses_CSV(BasicTypes.Response, "./assist/temp.csv"))
        resp._convert_input = conv.convert_input

        return resp

    @pytest.mark.parametrize('input_value, response, grade, to_type, from_type',
                             [
                                 ("1", "0", GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 ("32", "0", GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
                                 ("1.2", "1.1", GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 # rounded
                                 ("1.256", "-17.08", GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
                                 ("1.256", "-17.077", GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
                                 ("1.256222", "-17.075", GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
                                 ("1.2565", "-17.076", GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
                                 ("1.256", "1.1222", GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 ("3.1499999999999999999", "3.2", GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 # negative
                                 ("-1.2", "-18.44444", GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
                                 ("-1.2", "-1.1", GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 # rounded negative
                                 ("-1.256", "-18.4755", GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
                                 ("-1.256", "-1.1222", GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 # invalid
                                 ("1.2", "1.2", GradeTypes.INVALID, 'dog', 'Farenheit'),
                                 ("1.2", "1.2", GradeTypes.INVALID, 'Celsius', 'dog'),
                                 ("1.2", "dog", GradeTypes.INVALID, 'Celsius', 'dog'),
                                 ("1.2", "dog", GradeTypes.INVALID, 'dog', 'Farenheit'),
                                 ("1.2", "dog", GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 ("dog", "1.2", GradeTypes.INCORRECT, 'Celsius', 'Farenheit')
                             ])
    def test_get_response(self, input_value, response, grade, to_type, from_type):

        resp = self.setup_method()

        resp.add(Test_Response_VM.student_id, {
            "response": response,
            "input_value": input_value,
            "from_type": from_type,
            "to_type": to_type,
            "timestamp": Test_Response_VM.timestamp,
            "ID": ''
        }, persist=False)
        result = resp.get_response(from_type, to_type, Test_Response_VM.student_id, Test_Response_VM.timestamp)[0]

        assert result.response == response
        assert result.input_value == input_value        
        assert result.grade == grade
        assert result.from_type == from_type
        assert result.to_type == to_type
        assert result.student_id == Test_Response_VM.student_id
        assert result.timestamp == Test_Response_VM.timestamp

    @pytest.mark.parametrize('input_value, response, grade, to_type, from_type',
                             [
                                 ("1", "0", GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 ("32", "0", GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
                                 ("1.2", "1.1", GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 # rounded
                                 ("1.256", "-17.08", GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
                                 ("1.256", "-17.077", GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
                                 ("1.256222", "-17.075", GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
                                 ("1.2565", "-17.076", GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
                                 ("1.256", "1.1222", GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 ("3.1499999999999999999", "3.2", GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 # negative
                                 ("-1.2", "-18.44444", GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
                                 ("-1.2", "-1.1", GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 # rounded negative
                                 ("-1.256", "-18.4755", GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
                                 ("-1.256", "-1.1222", GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 # invalid
                                 ("1.2", "1.2", GradeTypes.INVALID, 'dog', 'Farenheit'),
                                 ("1.2", "1.2", GradeTypes.INVALID, 'Celsius', 'dog'),
                                 ("1.2", "dog", GradeTypes.INVALID, 'Celsius', 'dog'),
                                 ("1.2", "dog", GradeTypes.INVALID, 'dog', 'Farenheit'),
                                 ("1.2", "dog", GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 ("dog", "1.2", GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 ('', '32', GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 (None, '23', GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 ('23', '', GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 ('', '', GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 ("32", "0", GradeTypes.INVALID, '', 'Farenheit'),
                                 ("1.2", "1.1", GradeTypes.INVALID, 'Celsius', ''),
                                 ("32", "0", GradeTypes.INVALID, None, 'Farenheit'),
                                 ("1.2", "1.1", GradeTypes.INVALID, 'Celsius', None)
                             ])
    def test_add(self, input_value, response, grade, to_type, from_type):
        resp = self.setup_method()

        result = resp.add(Test_Response_VM.student_id, {
            "response": response,
            "input_value": input_value,
            "from_type": from_type,
            "to_type": to_type,
            "timestamp": Test_Response_VM.timestamp,
            "ID": ''
        }, persist=False)

        assert result.response == response
        assert result.input_value == input_value        
        assert result.grade == grade
        assert result.from_type == from_type
        assert result.to_type == to_type
        assert result.student_id == Test_Response_VM.student_id
        assert result.timestamp == Test_Response_VM.timestamp


    @pytest.mark.parametrize('input_value, response, grade, to_type, from_type',
                             [
                                 ("1", "0", GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 ("32", "0", GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
                                 ("1.2", "1.1", GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 # rounded
                                 ("1.256", "-17.08", GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
                                 ("1.256", "-17.077", GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
                                 ("1.256222", "-17.075", GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
                                 ("1.2565", "-17.076", GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
                                 ("1.256", "1.1222", GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 ("3.1499999999999999999", "3.2", GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 # negative
                                 ("-1.2", "-18.44444", GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
                                 ("-1.2", "-1.1", GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 # rounded negative
                                 ("-1.256", "-18.4755", GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
                                 ("-1.256", "-1.1222", GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 # invalid
                                 ("1.2", "1.2", GradeTypes.INVALID, 'dog', 'Farenheit'),
                                 ("1.2", "1.2", GradeTypes.INVALID, 'Celsius', 'dog'),
                                 ("1.2", "dog", GradeTypes.INVALID, 'Celsius', 'dog'),
                                 ("1.2", "dog", GradeTypes.INVALID, 'dog', 'Farenheit'),
                                 ("1.2", "dog", GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 ("dog", "1.2", GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 ('', '32', GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 (None, '23', GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 ('23', '', GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 ('', '', GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 ("32", "0", GradeTypes.INVALID, '', 'Farenheit'),
                                 ("1.2", "1.1", GradeTypes.INVALID, 'Celsius', ''),
                                 ("32", "0", GradeTypes.INVALID, None, 'Farenheit'),
                                 ("1.2", "1.1", GradeTypes.INVALID, 'Celsius', None)
                             ])
    def test_grade_input_value(self, input_value, response, grade, to_type, from_type):
        r = self.setup_method()

        input_value_rounded, input_value_calculated, input_value_grade = r.grade_input_value(from_type, to_type, response, input_value)

        assert input_value_grade == grade


    @pytest.mark.parametrize('input_value, response, grade, to_type, from_type',
                             [
                                 ("1", "0", GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 ("32", "0", GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
                                 ("1.2", "1.1", GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 # rounded
                                 ("1.256", "-17.08", GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
                                 ("1.256", "-17.077", GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
                                 ("1.256222", "-17.075", GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
                                 ("1.2565", "-17.076", GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
                                 ("1.256", "1.1222", GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 ("3.1499999999999999999", "3.2", GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 # negative
                                 ("-1.2", "-18.44444", GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
                                 ("-1.2", "-1.1", GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 # rounded negative
                                 ("-1.256", "-18.4755", GradeTypes.CORRECT, 'Celsius', 'Farenheit'),
                                 ("-1.256", "-1.1222", GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 # invalid
                                 ("1.2", "1.2", GradeTypes.INVALID, 'dog', 'Farenheit'),
                                 ("1.2", "1.2", GradeTypes.INVALID, 'Celsius', 'dog'),
                                 ("1.2", "dog", GradeTypes.INVALID, 'Celsius', 'dog'),
                                 ("1.2", "dog", GradeTypes.INVALID, 'dog', 'Farenheit'),
                                 ("1.2", "dog", GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 ("dog", "1.2", GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 ('', '32', GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 (None, '23', GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 ('23', '', GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 ('', '', GradeTypes.INCORRECT, 'Celsius', 'Farenheit'),
                                 ("32", "0", GradeTypes.INVALID, '', 'Farenheit'),
                                 ("1.2", "1.1", GradeTypes.INVALID, 'Celsius', ''),
                                 ("32", "0", GradeTypes.INVALID, None, 'Farenheit'),
                                 ("1.2", "1.1", GradeTypes.INVALID, 'Celsius', None)
                             ])
    # included all input params here to prove that the values doe not matter for not having a method defined
    def test_grade_input_value_error(self, input_value, response, grade, to_type, from_type):
        with pytest.raises(ModuleNotFoundError) as resultError:
            r = self.setup_method()
            r._convert_input = None

            r.grade_input_value(from_type, to_type, response, input_value)
        assert resultError.match("Please set a handler for converting input before calling Response_VM.grade_input_value")
