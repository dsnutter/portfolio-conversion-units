
from dependency_injector.wiring import Provide, inject
from ..di import Container
from ..View_Model import Response_VM, Conversion_VM
from ..helpers.View_Functions import View_Functions
from ..helpers.functions import Functions
from . import Response_Input_View, Response_Output_View, Conversion_View

#
# Input view functions
#
class Response_Input_View:

    @inject
    def Entry_Response_Type_DI(r_vm: Response_VM.Response_VM = Provide(Container.Container.reponses_vm),
                                c_vm: Conversion_VM.Conversion_VM = Provide(Container.Container.conversions_vm)):
        Response_Input_View.Entry_Response_Type(r_vm, c_vm)

    def Entry_Response_Type(r_vm: Response_VM.Response_VM,
                                c_vm: Conversion_VM.Conversion_VM):
        title = '** Please choose a response type **'
        menu_hashmap = {}
        for type in c_vm.all_types:
            menu_hashmap[type[0].lower()] = {
                'text': type,
                'execute': lambda t, c, r: Response_Input_View.Entry_Of_Multi_Reponse(t, r, c),
                'context': type
            }
        menu_hashmap['b'] = {
            'text': 'Back',
            'execute': ''
        }
        View_Functions.execute_menu(title, menu_hashmap, 'b', c_vm, r_vm)

    @inject
    def Entry_Of_Multi_Reponse_DI(type: str, 
                                r_vm: Response_VM.Response_VM = Provide(Container.Container.reponses_vm),
                                c_vm: Conversion_VM.Conversion_VM = Provide(Container.Container.conversions_vm)):
        Response_Input_View.Entry_Of_Multi_Reponse(type, r_vm, c_vm)

    def Entry_Of_Multi_Reponse(type: str, 
                                r_vm: Response_VM.Response_VM,
                                c_vm: Conversion_VM.Conversion_VM):

        title = f'** Student {type.capitalize()} Units Conversion Application **'
        menu_hashmap = {
                # display conversions
                'l': {
                    'text': 'List all possible conversion types',
                    'execute': lambda t, c, r: Conversion_View.Conversion_View.List_By_Conversion_Type(t, r, c),
                    'context': type
                },
                # enter responses
                'r': {
                    'text': 'Enter repsonses',
                    'execute': lambda t, c, r: Response_Input_View.Entry_Of_Single_Reponse(t, r, c),
                    'context': type
                },
                # quit application
                'b': {
                    'text': 'Back',
                    'execute': ''
                }
            }
        View_Functions.execute_menu(title, menu_hashmap, 'b', c_vm, r_vm)

    # filename = Main_View.Enter_Filename("saving to disk")
    # Configurations.Configurations.save_responses_dict_to_file({ type:  r_vm.get_responses() }, filename, BackendTypes.CSV)

    @inject
    def Entry_Of_Single_Reponse_DI(type: str, 
                                r_vm: Response_VM.Response_VM = Provide(Container.Container.reponses_vm),
                                c_vm: Conversion_VM.Conversion_VM = Provide(Container.Container.conversions_vm)):
        Response_Input_View.Entry_Of_Single_Reponse_NonDI(type, r_vm, c_vm)


    def Entry_Of_Single_Reponse(type: str, 
                                r_vm: Response_VM.Response_VM,
                                c_vm: Conversion_VM.Conversion_VM):
        #
        # this template defines what to print when gathering reponse inputs and how to validate that input
        #
        template = {
            'student_id': { 
                'text': 'student\'s ID', 
                'depends_on_previous': False,
                'can_override_valid': False,
                'valid_args': 'alphanumeric',
                'valid': lambda x: Functions.is_valid_string(x),
                'convert': lambda x: x.upper()
            },
            'answer': {
                'text': 'answer of numerical value', 
                'depends_on_previous': False,
                'can_override_valid': False,
                'valid_args': 'float',
                'valid': lambda x: Functions.is_valid_float(x),
                'convert': lambda x: x
            },
            'from_type': {
                'text': 'input unit of measure',
                'depends_on_previous': False,
                'can_override_valid': True,
                'valid_args': f'An item that is one of {str(c_vm.all_keys())}',
                'valid': lambda x: x in c_vm.all_keys(),
                'convert': lambda x: x.lower().capitalize()
            },
            'to_type': {
                'text': 'target unit of measure',
                'depends_on_previous': True,
                'can_override_valid': True,
                'valid_args': lambda x: f"An item that is one of {str(c_vm.all_keys_level2(x))}.\nIf you chose an invalid input unit of measure, you may not have choices",
                'valid': lambda entered, previous: entered in c_vm.all_keys_level2(previous),
                'convert': lambda x: x.lower().capitalize()
            },
            'response': {
                'text': 'student response of numerical value',
                'depends_on_previous': False,
                'can_override_valid': False,
                'valid_args': 'float',
                'valid': lambda x: Functions.is_valid_float(x),
                'convert': lambda x: x
            }
        }
        r = {}
        print(f'\n\nFor the reponse to a {type} conversion:')
        items = list(template.keys())
        i = 0
        while i < len(items):
            item = items[i]
            entered = None
            valid_entered = False
            valid_entered_with_previous = False
            override = False
            while entered is None or (not valid_entered and not valid_entered_with_previous):
                if entered is not None:
                    if template[item]['depends_on_previous'] and callable(template[item]['valid_args']):
                        valid_args = template[item]['valid_args'](previous)
                    else:
                        valid_args = template[item]['valid_args']
                    print(f"There was an error with your input it must be a valid {template[item]['text']} such as:")
                    print(f"{valid_args}")
                    if template[item]['can_override_valid']:
                        o_input = input(f"""
Press 'Y' to override and use the input that was entered
-or-
Press 'B' to go back to the previous choice before this one
-or-
Press enter to go back and reenter""")
                        if o_input.lower() == 'y':
                            override = True
                        elif o_input.lower() == 'b':
                            i -= 1
                            item = items[i]
                if override:
                    valid_entered = True
                    valid_entered_with_previous = True
                    override = False
                else:
                    entered = input(f"What was the {template[item]['text']}: ")
                    entered = template[item]['convert'](entered)
                    valid_entered = (not(template[item]['depends_on_previous']) and template[item]['valid'](entered))
                    valid_entered_with_previous = (template[item]['depends_on_previous']) and template[item]['valid'](entered, previous)
            if item == 'student_id':
                student_id = entered
            else:
                r[item] = entered
            previous = entered
            print(r)
            print()
            i += 1
        r_vm.add(student_id, r)

