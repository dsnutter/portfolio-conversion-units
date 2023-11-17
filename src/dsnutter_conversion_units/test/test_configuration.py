import pytest
from ..di import Configurations
from ..helpers.Enums import BackendTypes
from ..helpers.Data_Functions import Data_Functions


class Test_Configuration:


    @pytest.mark.parametrize('filename, file_type, header, content', 
            [
                ('test/files/test-read-conversions.json', BackendTypes.JSON,'', """

{
    "temperature":
    {
            "Farenheit":
            {
                "Celsius": { "eq": "x + 1", "ID": null },
                "Kelvin": { "eq": "x + 2", "ID": null }
            }
    }
}

"""),
                ('test/files/test-read-conversions.csv', BackendTypes.CSV,"Type,From,To,equation,ID","temperature,Farenheit,Celsius,x + 1\ntemperature,Farenheit,Kelvin,x + 2,")
            ])
    def test_conversions_file_to_dict(self, filename: str, file_type: BackendTypes, header: str, content: str):

        # recreate a sample file
        with open(file=filename, mode='w+') as file:
            file.writelines(header + "\n")
            file.writelines(content + "\n")

        result = Data_Functions.conversions_file_to_dict(filename, file_type)

        assert 'temperature' in result
        assert len(result['temperature'].keys()) == 1
        assert 'Farenheit' in result['temperature'].keys()
        assert len(result['temperature']['Farenheit'].keys()) == 2
        assert 'Kelvin' in result['temperature']['Farenheit'].keys()
        assert 'Celsius' in result['temperature']['Farenheit'].keys()
        assert result['temperature']['Farenheit']['Celsius']['eq'] == 'x + 1' 
        assert result['temperature']['Farenheit']['Kelvin']['eq'] == 'x + 2'
        assert 'ID' in result['temperature']['Farenheit']['Celsius']
        assert 'ID' in result['temperature']['Farenheit']['Kelvin']

    @pytest.mark.parametrize('filename_read, filename_save, file_type', 
            [
                ('test/files/test-write-conversions.json', 'test/files/test-temp-write-conversions.json', BackendTypes.JSON),
                ('test/files/test-write-conversions.csv', 'test/files/test-temp-write-conversions.csv', BackendTypes.CSV)
            ])
    def test_save_conversion_dict_to_file(self, filename_read: str, filename_save: str, file_type: BackendTypes):

        obj = Configurations.Configurations(file_type, filename_read, None)
        original = obj.conversions_config

        Data_Functions.save_conversion_dict_to_file(original, filename_save, file_type)

        same_after_saving = Data_Functions.conversions_file_to_dict(filename_save, file_type)

        assert same_after_saving == original

    @pytest.mark.parametrize('filename, file_type, header, content', 
            [
                ('test/files/test-read-responses.json', BackendTypes.JSON,'',"""{
    "students": {
        "ABC123": [
            {
                "response": "32.0",
                "answer": "0",
                "from_type": "Celsius",
                "to_type": "Farenheit",
                "grade": "correct",
                "timestamp": "2023-10-01 04:00 PM",
                "ID": null
            },
            {
                "response": "84.2",
                "answer": "543.94",
                "from_type": "Farenheit",
                "to_type": "Rankine",
                "grade": "correct",
                "timestamp": "2023-10-02 01:00 PM",
                "ID": null
            },
            {
                "response": "111.554",
                "answer": "317.33",
                "from_type": "Kelvin",
                "to_type": "Farenheit",
                "grade": "incorrect",
                "timestamp": "2023-10-01 09:01 AM",
                "ID": null
            }
        ],
        "ABC1233": [
            {
                "response": "0",
                "answer": "32",
                "from_type": "Farenheit",
                "to_type": "Celsius",
                "grade": "correct",
                "timestamp": "2023-10-02 10:00 AM",
                "ID": null
            },
            {
                "response": "dog",
                "answer": "6.5",
                "from_type": "Farenheit",
                "to_type": "Rankine",
                "grade": "incorrect",
                "timestamp": "2023-10-03 03:00 PM",
                "ID": null
            }
        ]
    }
}"""),
                ('test/files/test-read-responses.csv', BackendTypes.CSV,"Type,student_id,response,answer,from_type,to_type,grade,timestamp,ID","""
students,ABC123,32.0,0,Celsius,Farenheit,correct,2023-10-01 04:00 PM,
students,ABC1233,0,32,Farenheit,Celsius,correct2023-10-02 10:00 AM,
students,ABC123,84.2,543.94,Farenheit,Rankine,correct,2023-10-02 01:00 PM,
students,ABC123,111.554,317.33,Kelvin,Farenheit,incorrect,2023-10-01 09:01 AM,
students,ABC1233,dog,6.5,Farenheit,Rankine,incorrect,2023-10-03 03:00 PM,
""")
            ])
    def test_responses_file_to_dict(self, filename: str, file_type: BackendTypes, header: str, content: str):
#"temperature,ABC123,32.0,0,Celsius,Farenheit,correct,2023-10-01 04:00 PM"
        # recreate a sample file
        with open(file=filename, mode='w+') as file:
            file.writelines(header + "\n")
            file.writelines(content + "\n")

        result = Data_Functions.responses_file_to_dict(filename, file_type)

        assert 'students' in result
        assert len(result['students'].keys()) == 2
        assert 'ABC123' in result['students'].keys()
        assert len(result['students']['ABC123']) == 3
        assert 'response' in result['students']['ABC123'][0].keys()
        assert 'timestamp' in result['students']['ABC123'][0].keys()
        assert float(result['students']['ABC123'][0]['response']) == float('32')
        assert float(result['students']['ABC123'][0]['answer']) == float('0')
        assert result['students']['ABC123'][0]['grade'] == 'correct'

    @pytest.mark.parametrize('filename_read, filename_save, file_type', 
            [
                ('test/files/test-write-responses.json', 'test/files/test-temp-write-responses.json', BackendTypes.JSON),
                ('test/files/test-write-responses.csv', 'test/files/test-temp-write-responses.csv', BackendTypes.CSV)
            ])
    def test_save_responses_dict_to_file(self, filename_read: str, filename_save: str, file_type: BackendTypes):

        obj = Configurations.Configurations(file_type, None, filename_read)
        original = obj.responses_config

        Data_Functions.save_responses_dict_to_file(original, filename_save, file_type)

        same_after_saving = Data_Functions.responses_file_to_dict(filename_save, file_type)

        assert same_after_saving == original
