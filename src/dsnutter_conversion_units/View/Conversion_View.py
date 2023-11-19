from dependency_injector.wiring import Provide, inject
from ..di import Container
from ..View_Model import Conversion_VM, Response_VM


class Conversion_View:
    @inject
    def All_Possible_Types_DI(c_vm: Conversion_VM.Conversion_VM = Provide(Container.Container.conversions_vm)) -> None:
        Conversion_View.All_Possible_Types(None, c_vm)

    def All_Possible_Types(r_vm: Response_VM.Response_VM, c_vm: Conversion_VM.Conversion_VM) -> None:
        items = c_vm.all_keys()
        print(f'All the possible conversion question_types for {c_vm.current_type.capitalize()}:')
        for from_type in items:
            Conversion_View.List_Specific_From_Types(from_type, r_vm, c_vm)

    def List_Specific_From_Types(question_type: str, r_vm: Response_VM.Response_VM, c_vm: Conversion_VM.Conversion_VM) -> None:
        print('From Type: {}'.format(question_type))
        convertTypes = c_vm.all_to_types(question_type)
        for to_type in convertTypes:
            obj = c_vm.get_conversion_single(question_type, to_type)
            print('\tCan be converted to Type: {}'.format(to_type))
            print('\tEquation: {}'.format(obj.equation))
            # print('\tID: {}'.format(obj.id))

    def List_Possible_Conversion_Type(question_type: str, r_vm: Response_VM.Response_VM, c_vm: Conversion_VM.Conversion_VM):
        print(f"Possible Conversion Types for {question_type}")
        from_types = c_vm.all_from_types
        for from_type in from_types:
            to_types = c_vm.all_to_types(from_type)
            for to_type in to_types:
                print(f'\t{from_type} -> {to_type}')
