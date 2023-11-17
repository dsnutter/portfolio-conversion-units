
from .DI_Wireup import DI_Wireup
from ..View import Main_View
from ..helpers.Enums import BackendTypes
from ..helpers import settings

def run_as_app():
    wire = DI_Wireup(BackendTypes.CSV, settings.main_configurations)

    Main_View.Main_View.Main_Menu(wire)

