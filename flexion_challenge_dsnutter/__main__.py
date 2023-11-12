from dsnutter_conversion_units.di.Conversion_Container import Conversion_Container
from dsnutter_conversion_units.view import Conversion_View
from dsnutter_conversion_units.controller import Conversion_Controller, ImportExport_Controller
from dsnutter_conversion_units.helpers.Enums import FileTypes

import_con = ImportExport_Controller.Import_Export_Config_Controller(FileTypes.JSON, 'dsnutter_conversion_units/configuration/conversions_config.json', None)

config = import_con.conversions

# setups up injection of temperature conversion models derived from JSON files
temperature = Conversion_Container(config={'item': 'temperature', 'definitions': config})

# wires the views to the models, and depenency injection auto-creates the models when they are neededd
temperature.wire(modules=[Conversion_View.Conversion_View.All_Possible_Types])

# execute the view
Conversion_View.Conversion_View.All_Possible_Types()