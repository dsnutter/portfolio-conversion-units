import pytest
from dsnutter_conversion_units.di import Configurations
from dsnutter_conversion_units.Model.Conversion import Conversion
from dsnutter_conversion_units.helpers.Enums import FileTypes

class Test_Configuration:


    @pytest.mark.parametrize('filename, file_type, header, content', 
            [
                ('tests/temp_space/test-read.json', FileTypes.JSON,'',"{ \n\"temperature\":\n { \"Farenheit\": { \"Celsius\": \"x + 1\", \n\"Kelvin\": \"x + 2\" \n} \n} \n}"),
                ('tests/temp_space/test-read.csv', FileTypes.CSV,"TypeConversion,From,To,equation","temperature,Farenheit,Celsius,x + 1\ntemperature,Farenheit,Kelvin,x + 2")
            ])
    def test_conversions_file_to_dict(self, filename: str, file_type: FileTypes, header: str, content: str):

        # recreate a sample file
        with open(file=filename, mode='w+') as file:
            file.writelines(header + "\n")
            file.writelines(content + "\n")

        result = Configurations.Configurations.conversions_file_to_dict(filename, file_type)

        assert 'temperature' in result
        assert len(result['temperature'].keys()) == 1
        assert 'Farenheit' in result['temperature'].keys()
        assert len(result['temperature']['Farenheit'].keys()) == 2
        assert 'Kelvin' in result['temperature']['Farenheit'].keys()
        assert 'Celsius' in result['temperature']['Farenheit'].keys()
        assert result['temperature']['Farenheit']['Celsius'] == 'x + 1'
        assert result['temperature']['Farenheit']['Kelvin'] == 'x + 2'

    @pytest.mark.parametrize('filename_read, filename_save, file_type', 
            [
                ('tests/temp_space/test-write.json', 'tests/temp_space/test-temp-write.json', FileTypes.JSON),
                ('tests/temp_space/test-write.csv', 'tests/temp_space/test-temp-write.csv', FileTypes.CSV)
            ])
    def test_save_conversion_dict_to_file(self, filename_read: str, filename_save: str, file_type: FileTypes):

        obj = Configurations.Configurations(file_type, filename_read, None)
        original = obj.conversions_config

        obj.save_conversion_dict_to_file(filename_save, file_type)

        same_after_saving = Configurations.Configurations.conversions_file_to_dict(filename_save, file_type)

        assert same_after_saving == original

    # DSN Notes: needs implements when reponses is implemnted
    # def test_responses_file_to_dict(sfilename: str, file_type: FileTypes) -> dict:
    def test_responses_file_to_dict(self):

        assert 1 == 1

    # DSN Notes: needs implements when reponses is implemnted
    # def test_save_responses_config(self, filename: str, file_type: FileTypes):
    def test_save_responses_config(self):
        assert 1 == 1
