from ..Data import Data_Responses_CSV
from ..helpers.Enums import BackendTypes, BasicTypes, GradeTypes
from ..Model import Response

class Test_Data_Responses_CSV:
    filename = '../assist/temp.csv'
    type = BasicTypes.Response
    backend_type = BackendTypes.CSV
    ID = 'blah123'
    student_id = 'ABC123'

    def setup_method(self):
        response = Response.Response(Test_Data_Responses_CSV.student_id, '12.3', '12.0', 'ThinkDifferent', 'Celsius', "2023-10-01 04:00 PM", 
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
        assert 'ThinkDifferent' in from_types
        assert 'Celsius' in to_types

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
        assert 'Thinkdifferent' in from_types
        assert 'Celsius' in to_types
