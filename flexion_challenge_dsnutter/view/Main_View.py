
from dependency_injector.wiring import Provide, inject
from ..di import Container, Configurations
from ..View_Model import Response_VM, Conversion_VM
from ..helpers.View_Functions import View_Functions
from ..helpers.Enums import BackendTypes
from ..View import Conversion_View, Response_Input_View, Response_Output_View

class Main_View:

    main_menu = """
    
    
    """

    @inject
    def Main_Menu_DI(r_vm: Response_VM.Response_VM = Provide(Container.Container.reponses_vm),
                    c_vm: Conversion_VM.Conversion_VM = Provide(Container.Container.conversions_vm)):
        Main_View.Main_Menu(r_vm, c_vm)

    def Main_Menu(r_vm: Response_VM.Response_VM, c_vm: Conversion_VM.Conversion_VM):
        title = '** Student Units Conversion Application **'
        menu_hashmap = {
                # display responses
                'd': {
                    'text': 'Display all response entries [including previous ones] to screen',
                    'execute': lambda t, c, r: Response_Output_View.Response_Output_View.Display_Of_All_Responses(r, c)
                },
                # display conversions
                'c': {
                    'text': 'List all possible conversion types',
                    'execute': lambda t, c, r_vm: Conversion_View.Conversion_View.All_Possible_Types(r, c)
                },
                # enter responses
                'r': {
                    'text': 'Enter repsonses',
                    'execute': lambda t, c, r: Response_Input_View.Response_Input_View.Entry_Response_Type(r, c)
                },
                # quit application
                'q': {
                    'text': 'Quit',
                    'execute': ''
                }
            }
        # print(r_vm)
        View_Functions.execute_menu(title, menu_hashmap, 'q', c_vm, r_vm)


