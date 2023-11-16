from flexion_challenge_dsnutter.di.DI_Wireup import DI_Wireup
from flexion_challenge_dsnutter.View import Main_View
from flexion_challenge_dsnutter.helpers.Enums import BackendTypes
from .helpers import settings

wire = DI_Wireup(BackendTypes.CSV, settings.main_configurations)

Main_View.Main_View.Main_Menu(wire)

