from ..di.Configurations import Configurations
from .Enums import BackendTypes
import pkg_resources

conversions_filename = pkg_resources.resource_filename(__name__, '../configuration/conversions_config.csv')
responses_filename = pkg_resources.resource_filename(__name__, '../configuration/responses_config.csv')
conversions_filter_filename = pkg_resources.resource_filename(__name__, '../configuration/conversions_filter.csv')

print(conversions_filename)
print(responses_filename)
print(conversions_filter_filename)

file_type = BackendTypes.CSV

main_configurations = Configurations(file_type,
                                     conversions_filename,
                                     responses_filename,
                                     conversions_filter_filename)
