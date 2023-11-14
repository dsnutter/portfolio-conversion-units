
from dependency_injector.wiring import Provide, inject
from ..di import Container
from ..View_Model import Response_VM, Conversion_VM
from ..helpers.functions import Functions

class Response_View:

    #
    # Input view functions
    #
    @inject
    def Entry_Of_Single_Reponse(type: str, 
                                r_vm: Response_VM.Response_VM = Provide(Container.Container.reponses_vm),
                                c_vm: Conversion_VM.Conversion_VM = Provide(Container.Container.conversions_vm)):
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
                'valid_args': f'An item that is one of {str(c_vm.all_from_types)}',
                'valid': lambda x: x in c_vm.all_from_types,
                'convert': lambda x: x.lower().capitalize()
            },
            'to_type': {
                'text': 'target unit of measure',
                'depends_on_previous': True,
                'can_override_valid': True,
                'valid_args': lambda x: f"An item that is one of {str(c_vm.all_to_types(x))}.\nIf you chose an invalid input unit of measure, you may not have choices",
                'valid': lambda entered, previous: entered in c_vm.all_to_types(previous),
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
                        o_input = input(f'Press \'Y\' to override and use the input that was entered or press \'B\' to go back to the previous choice before this one...')
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
            r[item] = entered
            previous = entered
            print(r)
            print()
            i += 1
        r_vm.add_reponse(r)

    #
    # Output view functions
    #
    # this view is mainly for dev test purposes to see all responses that have been persisted already
    @inject
    def Display_Of_All_Responses(vm: Response_VM.Response_VM = Provide(Container.Container.reponses_vm)) -> None:
        vm.generate_preexisting_responses()
        items = vm.all_from_types
        print('\n\nAll the responses so far:')
        for from_type in items:
            print('\nFrom Type: {}'.format(from_type))
            to_types = vm.all_to_types(from_type)
            for to_type in to_types:
                students = vm.all_students(from_type, to_type)
                for student_id in students:                        
                    objs = vm.get_responses(from_type, to_type, student_id)
                    for obj in objs:
                        print(f'Student ID: {obj.student_id}')
                        print(f"""
Details
    From: {obj.from_type}
    To: {obj.to_type}
    Student Entered: {obj.response}
    Answer was: {obj.answer}
    Grade was: {obj.grade}
    Timestamp: {obj.timestamp}
    ID: {obj.id}
""")

    @inject
    def Display_Of_Single_Reponse():
        pass

    # simple print commands
    @inject
    def Console_Summary():
        pass

    # jinja2 templating
    @inject
    def Text_Summary():
        pass

    # opens in chrome or firefox
    # jinja2 templating
    @inject
    def HTML_Summary():
        pass

    # possible future: am guessing there is a library for this for python somewheres
    #  could use a python latex library with jinja2 templating for this?
    @inject
    def PDF_Summary():
        pass

    # possible future if integrated with SQLAlchemy library with SQLite or some other SQL: graph of statistics of reponses such as a bar graph of incorrect, invalid, correct
    @inject
    def Display_Graph():
        pass

