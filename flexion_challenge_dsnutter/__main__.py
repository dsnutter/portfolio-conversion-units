from dsnutter_conversion_units.di.DI_Wireup import DI_Wireup
from dsnutter_conversion_units.View import Main_View
from dsnutter_conversion_units.helpers.Enums import BackendTypes
from .helpers import settings

wire = DI_Wireup(BackendTypes.CSV, settings.main_configurations)

Main_View.Main_View.Main_Menu(wire)

