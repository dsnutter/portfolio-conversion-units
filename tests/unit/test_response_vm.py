import pytest

from flexion_challenge_dsnutter.helpers.Enums import GradeTypes
from flexion_challenge_dsnutter.View_Model.Response_VM import Response_VM
from flexion_challenge_dsnutter.Model.Response import Response
from datetime import datetime

class Test_Response_VM:

    @pytest.mark.parametrize('response, answer, grade', 
        [
            ("1", 0, GradeTypes.INCORRECT),
            ("1.2", 1.2, GradeTypes.CORRECT),
            ("1.2", 1.1, GradeTypes.INCORRECT),
            # rounded
            ("1.256", 1.278, GradeTypes.CORRECT),
            ("1.256", 1.1222, GradeTypes.INCORRECT),
            # negative
            ("-1.2", -1.2, GradeTypes.CORRECT),
            ("-1.2", -1.1, GradeTypes.INCORRECT),
            # rounded negative
            ("-1.256", -1.278, GradeTypes.CORRECT),
            ("-1.256", -1.1222, GradeTypes.INCORRECT),
        ])
    def test_grade(self, response, answer, grade):

        c = Response_VM('students', {
    "students": {
        "ABC123": [
            {
                "response": response,
                "answer": answer,
                "from_type": "Celsius",
                "to_type": "Farenheit",
                "grade": grade,
                "timestamp": "2023-10-01 04:00 PM"
            }
        ]}}, Response, True)

        c.grade_answer(response, answer)
        result = c.get_response('Celsius', 'Farenheit', 'ABC123', '2023-10-01 04:00 PM')
        assert result.grade == grade

