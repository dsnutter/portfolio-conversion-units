
from dependency_injector.wiring import Provide, inject
from ..di import Container
from ..View_Model import Response_VM

class Response_View:

    #
    # Input view functions
    #
    @inject
    def Entry_Of_Single_Reponse():
        pass



    #
    # Output view functions
    #
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

