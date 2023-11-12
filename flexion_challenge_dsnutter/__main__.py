from flexion_challenge_dsnutter.di.Conversion_Container import Conversion_Container
from flexion_challenge_dsnutter.di.Configurations import Configurations
from flexion_challenge_dsnutter.View import Conversion_View
from flexion_challenge_dsnutter.helpers.Enums import FileTypes


import_con = Configurations(FileTypes.JSON, 'flexion_challenge_dsnutter/configuration/conversions_config.json', None)

config = import_con.conversions

# setups up injection of temperature conversion Models derived from JSON files
temperature = Conversion_Container(config={'item': 'temperature', 'definitions': config})

# wires the views to the Models, and depenency injection auto-creates the Models when they are neededd
temperature.wire(modules=[Conversion_View.Conversion_View.All_Possible_Types])

# execute the view
Conversion_View.Conversion_View.All_Possible_Types()