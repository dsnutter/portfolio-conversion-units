from ..Data import Data_Responses_CSV
from ..helpers.Enums import BackendTypes, BasicTypes, GradeTypes
from ..Model import Response


class Test_Data_Responses_CSV:
    filename = '../assist/temp.csv'
    type = BasicTypes.Response
    backend_type = BackendTypes.CSV
    ID = 'blah123'
    student_id = 'ABC123'
    timestamp = "2023-10-01 04:00 PM"
    from_type = 'ThinkDifferent'
    to_type = 'Celsius'

    def setup_method(self):
        response = Response.Response(Test_Data_Responses_CSV.student_id, '12.3', '12.0',
                                     Test_Data_Responses_CSV.from_type,
                                     Test_Data_Responses_CSV.to_type,
                                     Test_Data_Responses_CSV.timestamp,
                                     GradeTypes.INCORRECT, Test_Data_Responses_CSV.ID, 12.2, 12.222222)
        return response

    def test_to_dataframe_all(self):
        response = self.setup_method()

        obj = Data_Responses_CSV.Data_Responses_CSV(Test_Data_Responses_CSV.backend_type, Test_Data_Responses_CSV.filename)
        obj.add_with_student_id('temperature', Test_Data_Responses_CSV.student_id, response, persist=False)
        df = obj.to_dataframe_all(for_display=False)

        IDs = df['ID'].values
        student_IDs = df['student_id'].values
        from_types = df['from_type'].values
        to_types = df['to_type'].values

        assert Test_Data_Responses_CSV.ID in IDs
        assert Test_Data_Responses_CSV.student_id in student_IDs
        assert Test_Data_Responses_CSV.from_type in from_types
        assert Test_Data_Responses_CSV.to_type in to_types

    def test_to_dataframe_all_for_display(self):
        response = self.setup_method()

        obj = Data_Responses_CSV.Data_Responses_CSV(Test_Data_Responses_CSV.backend_type, Test_Data_Responses_CSV.filename)
        obj.add_with_student_id('temperature', Test_Data_Responses_CSV.student_id, response, persist=False)
        df = obj.to_dataframe_all(for_display=True)

        student_IDs = df['student_id'].values
        from_types = df['from_type'].values
        to_types = df['to_type'].values

        assert 'ID' not in df.keys()
        assert Test_Data_Responses_CSV.student_id in student_IDs
        assert Test_Data_Responses_CSV.from_type.lower().capitalize() in from_types
        assert Test_Data_Responses_CSV.to_type in to_types

    def test_get_response_same_student(self):
        response = self.setup_method()

        obj = Data_Responses_CSV.Data_Responses_CSV(Test_Data_Responses_CSV.backend_type, Test_Data_Responses_CSV.filename)
        obj.add_with_student_id('temperature', Test_Data_Responses_CSV.student_id, response, persist=False)
        obj.add_with_student_id('temperature', Test_Data_Responses_CSV.student_id, response, persist=False)

        resp = obj.get_response('ThinkDifferent', 'Celsius', Test_Data_Responses_CSV.student_id,
                                Test_Data_Responses_CSV.timestamp)

        assert resp[0].id == response.id
        assert resp[0].student_id == response.student_id
        assert resp[0].from_type == response.from_type
        assert resp[0].to_type == response.to_type
        assert resp[0].response == response.response
        assert resp[0].input_value == response.input_value

        assert resp[1].id == response.id
        assert resp[1].student_id == response.student_id
        assert resp[1].from_type == response.from_type
        assert resp[1].to_type == response.to_type
        assert resp[1].response == response.response
        assert resp[1].input_value == response.input_value

    def test_get_response_different_students(self):
        response = self.setup_method()

        obj = Data_Responses_CSV.Data_Responses_CSV(Test_Data_Responses_CSV.backend_type, Test_Data_Responses_CSV.filename)
        obj.add_with_student_id('temperature', Test_Data_Responses_CSV.student_id, response, persist=False)
        obj.add_with_student_id('temperature', Test_Data_Responses_CSV.student_id, response, persist=False)

        response2 = self.setup_method()
        response2.student_id = 'cat'
        obj.add_with_student_id('temperature', 'cat', response2, persist=False)

        resp = obj.get_response('ThinkDifferent', 'Celsius', 'cat', Test_Data_Responses_CSV.timestamp)

        assert resp[0].id == response2.id
        assert resp[0].student_id == 'cat'.upper()
        assert resp[0].from_type == response2.from_type
        assert resp[0].to_type == response2.to_type
        assert resp[0].response == response2.response
        assert resp[0].input_value == response2.input_value
