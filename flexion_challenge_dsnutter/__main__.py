from flexion_challenge_dsnutter.di.Conversion_Container import Conversion_Container
from flexion_challenge_dsnutter.helpers.helpers import to_json
from flexion_challenge_dsnutter.view import Conversion_View


config_file = 'flexion_challenge_dsnutter/configuration/conversions_config.json'

conversions_config = to_json(config_file)

# conversions_con = Conversion_Container(config={'definitions': temperature_config})

temperature = Conversion_Container(config={'item': 'temperature', 'definitions': conversions_config})

# print(temperature)

# conversion = temperature.conversions_many

# print(str(conversion))

temperature.wire(modules=[Conversion_View.All_Possible_Types])

Conversion_View.All_Possible_Types()