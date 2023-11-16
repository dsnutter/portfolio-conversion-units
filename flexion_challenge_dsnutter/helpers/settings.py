from ..di.Configurations import Configurations
from .Enums import BackendTypes

conversions_filename = 'flexion_challenge_dsnutter/configuration/conversions_config.csv'
responses_filename = 'flexion_challenge_dsnutter/configuration/responses_config.csv'

file_type = BackendTypes.CSV

main_configurations = Configurations(file_type, 
                        conversions_filename, 
                        responses_filename)

