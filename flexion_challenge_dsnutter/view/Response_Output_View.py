
from dependency_injector.wiring import Provide, inject
from ..di import Container
from ..View_Model import Response_VM, Conversion_VM
from ..helpers.functions import Functions

#
# Output view functions
#
class Response_Output_View:

    @inject
    def Display_Of_All_Responses_DI(vm: Response_VM.Response_VM = Provide(Container.Container.reponses_vm)) -> None:
        Response_Output_View.Display_Of_All_Responses(vm, None)

    # this view is mainly for dev test purposes to see all responses that have been persisted already
    def Display_Of_All_Responses(r_vm: Response_VM.Response_VM, c_vm: Conversion_VM.Conversion_VM) -> None:
        # r_vm.execute_load_preexisting()
        items = r_vm.all_keys()
        print('\n\nAll the responses so far:\n')
        for student_id in items:                        
            objs = r_vm.get_responses(student_id)
            for obj in objs:
                Response_Output_View.Display_Of_Single_Reponse(obj)

    def Display_Of_Single_Reponse(obj: Response_VM.Response_VM):
                print(f'\nStudent ID: {obj.student_id}')
                print(f"""Details
    From: {obj.from_type}
    To: {obj.to_type}
    Student Entered: {obj.response}
    Answer was: {obj.answer}
    Grade was: {obj.grade}
    Timestamp: {obj.timestamp}
    ID: {obj.id}

""")

    # simple print commands
    @inject
    def Console_Summary_DI():
        pass

    # possible future: jinja2 templating
    @inject
    def Text_Summary_DI():
        pass

    # opens in chrome or firefox
    # possible future: jinja2 templating
    @inject
    def HTML_Summary_DI():
        pass

    # possible future: am guessing there is a library for this for python somewheres
    #  could use a python latex library with jinja2 templating for this?
    @inject
    def PDF_Summary_DI():
        pass

    # possible future if integrated with SQLAlchemy library with SQLite or some other SQL: graph of statistics of reponses such as a bar graph of incorrect, invalid, correct
    @inject
    def Display_Graph_DI():
        pass

