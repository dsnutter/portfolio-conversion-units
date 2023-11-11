from flexion_challenge_dsnutter.di.Conversion_Container import Conversion_Container
from flexion_challenge_dsnutter.view import Conversion_View
from flexion_challenge_dsnutter.controller import Conversion_Controller, Import_Controller

import_con = Import_Controller.Import_Controller('flexion_challenge_dsnutter/configuration/conversions_config.json')

config = import_con.get_conversions_config
# setups up injection of temperature conversion models derived from JSON files
temperature = Conversion_Container(config={'item': 'temperature', 'definitions': config})

# wires the views to the models, and depenency injection auto-creates the models when they are neededd
temperature.wire(modules=[Conversion_View.All_Possible_Types])

# execute the view
Conversion_View.All_Possible_Types()