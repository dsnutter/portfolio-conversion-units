
from dependency_injector.wiring import Provide, inject
from ..di import Container, DI_Wireup
from ..View_Model import Response_VM, Conversion_VM
from ..helpers.View_Functions import View_Functions
from ..helpers.functions import Functions
from . import Conversion_View

#
# Input view functions
#


class Response_Input_View:

    @inject
    def Entry_Response_Type_DI():
        Response_Input_View.Entry_Response_Type()

    def Entry_Response_Type(config: DI_Wireup.DI_Wireup):
        title = '** Please choose a response question_type **'
        menu_hashmap = {}
        for question_type in config.types:
            menu_hashmap[question_type[0].lower()] = {
                'text': question_type,
                'execute': lambda t, c, r: Response_Input_View.wire_input_responses(t, config),
                'context': question_type
            }
        menu_hashmap['b'] = {
            'text': 'Back',
            'execute': ''
        }
        menu_hashmap['q'] = {
            'text': 'Quit',
            'execute': ''
        }
        while View_Functions.execute_menu(config, title, menu_hashmap, ['b', 'q'], None, None) and not config.halt:
            pass

    def wire_input_responses(question_type: list, config: DI_Wireup.DI_Wireup):
        modules = [Response_Input_View.Entry_Of_Multi_Reponse_DI]

        config.wire_up(question_type, modules)
        Response_Input_View.Entry_Of_Multi_Reponse_DI(config, question_type)

    @inject
    def Entry_Of_Multi_Reponse_DI(wire: DI_Wireup.DI_Wireup, question_type: str,
                                  r_vm: Response_VM.Response_VM = Provide(Container.Container.reponses_vm),
                                  c_vm: Conversion_VM.Conversion_VM = Provide(Container.Container.conversions_vm)):
        # to hook up calculations and other stuff
        r_vm.setup_conversions(c_vm)

        Response_Input_View.Entry_Of_Multi_Reponse(wire, question_type, r_vm, c_vm)

    def Entry_Of_Multi_Reponse(wire: DI_Wireup.DI_Wireup, question_type: str,
                               r_vm: Response_VM.Response_VM,
                               c_vm: Conversion_VM.Conversion_VM):

        title = f'** Student {question_type.capitalize()} Units Conversion Application **'
        menu_hashmap = {
            # display conversions
            'l': {
                'text': f'List all possible conversion question types for {question_type.capitalize()}',
                'execute': lambda t, c, r: Conversion_View.Conversion_View.List_Possible_Conversion_Type(t, r, c),
                'context': question_type
            },
            # enter responses
            'e': {
                'text': 'Enter response',
                'execute': lambda t, c, r: Response_Input_View.Entry_Of_Single_Reponse(t, r, c),
                'context': question_type
            },
            # quit application
            'b': {
                'text': 'Back',
                'execute': ''
            },
            'q': {
                'text': 'quit',
                'execute': ''
            }
        }
        while View_Functions.execute_menu(wire, title, menu_hashmap, ['b', 'q'], c_vm, r_vm) and not wire.halt:
            pass

    @inject
    def Entry_Of_Single_Reponse_DI(question_type: str,
                                   r_vm: Response_VM.Response_VM = Provide(Container.Container.reponses_vm),
                                   c_vm: Conversion_VM.Conversion_VM = Provide(Container.Container.conversions_vm)):
        Response_Input_View.Entry_Of_Single_Reponse_NonDI(question_type, r_vm, c_vm)

    def Entry_Of_Single_Reponse(question_type: str,
                                r_vm: Response_VM.Response_VM,
                                c_vm: Conversion_VM.Conversion_VM):
        template = Response_Input_View.Entry_Single_Response_Template(question_type, r_vm, c_vm)
        r = {}
        print(f'\n\nFor the reponse to a {question_type} conversion:')
        template_keys = list(template.keys())
        i = 0
        previous = ''
        while i < len(template_keys):
            key = template_keys[i]
            entered = None
            valid_entered = False
            valid_entered_with_previous = False
            override = False
            while entered is None or (not valid_entered and not valid_entered_with_previous):
                if entered is not None:
                    override = Response_Input_View. \
                        Entry_Single_Response_Handle_Errors(template,
                                                            previous,
                                                            key)
                if override:
                    valid_entered = True
                    valid_entered_with_previous = True
                    override = False
                else:
                    valid_entered, valid_entered_with_previous, entered = Response_Input_View. \
                        Entry_Single_Response_Handle_General_Input(
                            template,
                            key,
                            previous)
            if key == 'student_id':
                student_id = entered
            else:
                r[key] = entered
            previous = entered
            i += 1
        try:
            result = r_vm.add(student_id, r)
        except Exception as ex:
            print(ex)

        if len(result.filter_result_msg) > 0:
            print(f"""
The result for {result.student_id} is not possible given the input value {result.input_value} \
and student response {result.response} since:

{str.join(", ", result.filter_result_msg)}.

The response you entered was not saved.
""")
        elif result.grade:
            print(f"\nThe graded result for student {result.student_id} is: {result.grade_for_display}\n")

    def Entry_Single_Response_Handle_Errors(template, previous, template_key):
        override = False

        if template[template_key]['depends_on_previous'] and callable(template[template_key]['valid_args']):
            valid_args = template[template_key]['valid_args'](previous)
        else:
            valid_args = template[template_key]['valid_args']
        print(f"There was an error with your input it must be a valid {template[template_key]['text']} such as:")
        print(f"{valid_args}")
        if template[template_key]['can_override_valid']:
            o_input = input("""
Press enter to go back and reenter
-or-
Press 'Y' to override and use what was entered
""")
            if o_input.lower() == 'y':
                override = True
        return override

    def Entry_Single_Response_Handle_General_Input(template, item, previous):
        entered = input(f"What was the {template[item]['text']}: ")
        entered = template[item]['convert'](entered)

        valid_entered = (not (template[item]['depends_on_previous']) and template[item]['valid'](entered))
        valid_entered_with_previous = (template[item]['depends_on_previous']) and template[item]['valid'](entered, previous)

        return valid_entered, valid_entered_with_previous, entered

    def Entry_Single_Response_Template(question_type: str,
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
            'input_value': {
                'text': 'input value for equation of numerical value',
                'depends_on_previous': False,
                'can_override_valid': True,
                'valid_args': 'float',
                'valid': lambda x: Functions.is_valid_float(x),
                'convert': lambda x: x
            },
            'from_type': {
                'text': 'input unit of measure',
                'depends_on_previous': False,
                'can_override_valid': True,
                'valid_args': f'An item that is one of ({", ".join(c_vm.all_keys()).replace("_", " ")})',
                'valid': lambda x: x in c_vm.all_keys(),
                'convert': lambda x: x.lower().capitalize().replace(' ', '_')
            },
            'to_type': {
                'text': 'target unit of measure',
                'depends_on_previous': True,
                'can_override_valid': True,
                'valid_args': lambda x: f"""An item that is one of ({', '.join(c_vm.all_to_types(x)).replace('_', ' ')}).
If you chose an invalid input unit of measure, you may not have choices""",
                'valid': lambda entered, previous: entered in c_vm.all_to_types(previous),
                'convert': lambda x: x.lower().capitalize().replace(' ', '_')
            },
            'response': {
                'text': 'student response of numerical value',
                'depends_on_previous': False,
                'can_override_valid': True,
                'valid_args': 'float',
                'valid': lambda x: Functions.is_valid_float(x),
                'convert': lambda x: x
            }
        }
        return template
