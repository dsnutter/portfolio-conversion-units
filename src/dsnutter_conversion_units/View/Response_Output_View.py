
from dependency_injector.wiring import Provide, inject
from ..di import Container
from ..View_Model import Response_VM, Conversion_VM
from ..Model import Response

#
# Output view functions
#


class Response_Output_View:

    @inject
    def Display_Of_All_Responses_DI(r_vm: Response_VM.Response_VM = Provide(Container.Container.reponses_vm)) -> None:
        Response_Output_View.Display_Of_All_Responses(r_vm, None)

    # this view loads all previous responses and displays them
    def Display_Of_All_Responses(r_vm: Response_VM.Response_VM, c_vm: Conversion_VM.Conversion_VM) -> None:
        r_vm.execute_load_preexisting()
        items = r_vm.all_keys()
        print(f'\n\nAll the responses so far for {r_vm.current_type}:\n')
        for student_id in items:
            objs = r_vm.get_responses(student_id)
            for obj in objs:
                Response_Output_View.Display_Of_Single_Response(obj)

    def Display_Of_Single_Response(obj: Response.Response):
        print(f'\nStudent ID: {obj.student_id}')
        print(f"""Details
    From: {obj.from_type}
    To: {obj.to_type}
    Student Entered: {obj.response}
    input_value was: {obj.input_value}
    Grade was: {obj.grade}
    Timestamp: {obj.timestamp}
    ID: {obj.id}

""")

    # print table to console
    @inject
    def Console_Summary_DI(r_vm: Response_VM.Response_VM = Provide(Container.Container.reponses_vm)):
        Response_Output_View.Display_Summary_Console(r_vm, None)

    # this view loads all previous responses and displays them
    def Display_Summary_Console(r_vm: Response_VM.Response_VM, c_vm: Conversion_VM.Conversion_VM) -> None:
        r_vm.execute_load_preexisting()
        print(f'\n\nAll the responses so far for {r_vm.current_type}:')
        print(r_vm.to_dataframe_all(for_display=True).to_markdown())

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

    # possible future if integrated with SQLAlchemy library with SQLite or some other SQL: 
    # graph of statistics of reponses such as a bar graph of incorrect, invalid, correct
    @inject
    def Display_Graph_DI():
        pass
