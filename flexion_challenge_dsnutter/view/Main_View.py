
from dependency_injector.wiring import Provide, inject
from ..di import Container, Configurations as config_di
from ..helpers.View_Functions import View_Functions
from ..View import Conversion_View, Response_Input_View, Response_Output_View

class Main_View:

    def Main_Menu(config: config_di.Configurations):
        title = '** Student Units Conversion Application **'
        types = config.types
        menu_hashmap = {
                # display responses
                'd': {
                    'text': 'Display all response entries [including previous ones] to screen',
                    'execute': lambda t, c, r: Main_View.wire_display_responses(types, config)
                },
                # display conversions
                'c': {
                    'text': 'List all possible conversion types',
                    'execute': lambda t, c, r: Main_View.wire_display_conversions(types, config)
                },
                # enter responses
                'r': {
                    'text': 'Enter repsonses',
                    'execute': lambda t, c, r: Response_Input_View.Response_Input_View.Entry_Response_Type(config)
                },
                # quit application
                'q': {
                    'text': 'Quit',
                    'execute': ''
                }
            }
        # print(r_vm)
        View_Functions.execute_menu(title, menu_hashmap, 'q', None, None)

    def wire_display_responses(types: list, config: config_di.Configurations):
        modules = [Response_Output_View.Response_Output_View.Display_Of_All_Responses_DI]
        for type in types:
            config.wire_up(type, modules)
            Response_Output_View.Response_Output_View.Display_Of_All_Responses_DI()

    def wire_display_conversions(types: list, config: config_di.Configurations):
        modules = [Conversion_View.Conversion_View.All_Possible_Types_DI]
        for type in types:
            config.wire_up(type, modules)
            Conversion_View.Conversion_View.All_Possible_Types_DI()