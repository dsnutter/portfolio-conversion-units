from dsnutter_conversion_units.di.Container import Container
from dsnutter_conversion_units.di.Configurations import Configurations
from dsnutter_conversion_units.View import Conversion_View, Response_View
from dsnutter_conversion_units.helpers.Enums import FileTypes


c_json = Configurations(FileTypes.JSON, 
                   'dsnutter_conversion_units/configuration/conversions_config.json', 
                   'dsnutter_conversion_units/configuration/responses_config.json')

#
# temperatures
#
# setups up injection of temperature/responses conversion Models derived from JSON files
container_json_temperature = Container(config_conversions={'item': 'temperature', 'definitions': c_json.conversions_config},
                        config_responses={'item': 'temperature', 'definitions': c_json.responses_config})

# wires the views to the Models, and depenency injection auto-creates the Models when they are neededd
container_json_temperature.wire(modules=[Conversion_View.Conversion_View.All_Possible_Types])

# wires the views to the Models, and depenency injection auto-creates the Models when they are neededd
container_json_temperature.wire(modules=[Response_View.Response_View.Display_Of_All_Responses])

# execute the view for temperatures
Conversion_View.Conversion_View.All_Possible_Types()

# execute the view for responses
Response_View.Response_View.Display_Of_All_Responses()

#
# volumes
#
# setups up injection of temperature/responses conversion Models derived from JSON files
container_json_volumes = Container(config_conversions={'item': 'volume', 'definitions': c_json.conversions_config},
                        config_responses={'item': 'volume', 'definitions': c_json.responses_config})

# wires the views to the Models, and depenency injection auto-creates the Models when they are neededd
container_json_volumes.wire(modules=[Conversion_View.Conversion_View.All_Possible_Types])

# wires the views to the Models, and depenency injection auto-creates the Models when they are neededd
container_json_volumes.wire(modules=[Response_View.Response_View.Display_Of_All_Responses])

# execute the view for temperatures
Conversion_View.Conversion_View.All_Possible_Types()

# execute the view for responses
Response_View.Response_View.Display_Of_All_Responses()

# convert the CSV config to JSON
#hash = Configurations.conversions_file_to_dict('dsnutter_conversion_units/configuration/conversions_config.csv', FileTypes.CSV)
#Configurations.save_conversion_dict_to_file(hash, './temp.json', FileTypes.JSON)

# convert the JSON confg to CSV
#hash = Configurations.conversions_file_to_dict('dsnutter_conversion_units/configuration/conversions_config.json', FileTypes.JSON)
#Configurations.save_conversion_dict_to_file(hash, './temp.csv', FileTypes.CSV)

# Responses, CSV to JSON
#hash = Configurations.responses_file_to_dict('dsnutter_conversion_units/configuration/responses_config.csv', FileTypes.CSV)
#Configurations.save_responses_dict_to_file(hash, './temp.json', FileTypes.JSON)


# c_csv = Configurations(FileTypes.CSV, 
#                        'dsnutter_conversion_units/configuration/conversions_config.csv', 
#                        'dsnutter_conversion_units/configuration/responses_config.csv')


