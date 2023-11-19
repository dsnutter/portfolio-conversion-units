
from ..di import DI_Wireup
from ..helpers.View_Functions import View_Functions
from ..View import Conversion_View, Response_Input_View, Response_Output_View


class Main_View:

    def Main_Menu(wire: DI_Wireup.DI_Wireup):
        title = '\n** Student Units Conversion Application **'
        question_types = wire.types
        menu_hashmap = {
            # display responses
            'd': {
                'text': 'Display all response entries [including previous ones] to screen',
                'execute': lambda t, c, r: Main_View.wire_display_responses(question_types, wire)
            },
            # display conversions
            'c': {
                'text': 'List all conversion question_types details',
                'execute': lambda t, c, r: Main_View.wire_display_conversions(question_types, wire)
            },
            # enter responses
            'r': {
                'text': 'Responses actions',
                'execute': lambda t, c, r: Response_Input_View.Response_Input_View.Entry_Response_Type(wire)
            },
            # quit application
            'q': {
                'text': 'Quit',
                'execute': ''
            }
        }
        # print(r_vm)
        while View_Functions.execute_menu(wire, title, menu_hashmap, ['q'], None, None) and not wire.halt:
            pass

    def wire_display_responses(types: list, config: DI_Wireup.DI_Wireup):
        modules = [Response_Output_View.Response_Output_View.Console_Summary_DI]
        for question_type in types:
            config.wire_up(question_type, modules)
            Response_Output_View.Response_Output_View.Console_Summary_DI()

    def wire_display_conversions(types: list, config: DI_Wireup.DI_Wireup):
        modules = [Conversion_View.Conversion_View.All_Possible_Types_DI]
        for question_type in types:
            config.wire_up(question_type, modules)
            Conversion_View.Conversion_View.All_Possible_Types_DI()
