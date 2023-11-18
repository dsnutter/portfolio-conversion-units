from ..di.Configurations import Configurations
from .Enums import BackendTypes

conversions_filename = 'dsnutter_conversion_units/configuration/conversions_config.csv'
responses_filename = 'dsnutter_conversion_units/configuration/responses_config.csv'

file_type = BackendTypes.CSV

main_configurations = Configurations(file_type,
                                     conversions_filename,
                                     responses_filename)
