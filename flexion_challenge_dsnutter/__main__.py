from dsnutter_conversion_units.di.Container import Container
from dsnutter_conversion_units.di.Configurations import Configurations
from dsnutter_conversion_units.View import Conversion_View, Response_View
from dsnutter_conversion_units.helpers.Enums import FileTypes


c_json = Configurations(FileTypes.JSON, 
                   'dsnutter_conversion_units/configuration/conversions_config.json', 
                   'dsnutter_conversion_units/configuration/responses_config.json')

# setups up injection of temperature/responses conversion Models derived from JSON files
container_json = Container(config_conversions={'item': 'temperature', 'definitions': c_json.conversions_config},
                        config_responses={'item': 'students', 'definitions': c_json.responses_config})

# wires the views to the Models, and depenency injection auto-creates the Models when they are neededd
container_json.wire(modules=[Conversion_View.Conversion_View.All_Possible_Types])

# wires the views to the Models, and depenency injection auto-creates the Models when they are neededd
container_json.wire(modules=[Response_View.Response_View.Display_Of_All_Responses])

# execute the view for temperatures
Conversion_View.Conversion_View.All_Possible_Types()

# execute the view for responses
Response_View.Response_View.Display_Of_All_Responses()



# c_csv = Configurations(FileTypes.CSV, 
#                        'dsnutter_conversion_units/configuration/conversions_config.csv', 
#                        'dsnutter_conversion_units/configuration/responses_config.csv')


