from ..di.Configurations import Configurations
from .Enums import BackendTypes

conversions_filename = 'configuration/conversions_config.csv'
responses_filename = 'configuration/responses_config.csv'
conversions_filter_filename = 'configuration/conversions_filter.csv'

file_type = BackendTypes.CSV

main_configurations = Configurations(file_type,
                                     conversions_filename,
                                     responses_filename,
                                     conversions_filter_filename)
