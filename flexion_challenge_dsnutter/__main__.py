from flexion_challenge_dsnutter.di.Container import Container
from flexion_challenge_dsnutter.di.Configurations import Configurations
from flexion_challenge_dsnutter.View import Conversion_View, Response_View
from flexion_challenge_dsnutter.helpers.Enums import FileTypes


c_json = Configurations(FileTypes.JSON, 
                   'flexion_challenge_dsnutter/configuration/conversions_config.json', 
                   'flexion_challenge_dsnutter/configuration/responses_config.json')

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
#hash = Configurations.conversions_file_to_dict('flexion_challenge_dsnutter/configuration/conversions_config.csv', FileTypes.CSV)
#Configurations.save_conversion_dict_to_file(hash, './temp.json', FileTypes.JSON)

# convert the JSON confg to CSV
#hash = Configurations.conversions_file_to_dict('flexion_challenge_dsnutter/configuration/conversions_config.json', FileTypes.JSON)
#Configurations.save_conversion_dict_to_file(hash, './temp.csv', FileTypes.CSV)

# Responses, CSV to JSON
#hash = Configurations.responses_file_to_dict('flexion_challenge_dsnutter/configuration/responses_config.csv', FileTypes.CSV)
#Configurations.save_responses_dict_to_file(hash, './temp.json', FileTypes.JSON)


# c_csv = Configurations(FileTypes.CSV, 
#                        'flexion_challenge_dsnutter/configuration/conversions_config.csv', 
#                        'flexion_challenge_dsnutter/configuration/responses_config.csv')


