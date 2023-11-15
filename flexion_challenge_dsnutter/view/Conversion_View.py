from dependency_injector.wiring import Provide, inject
from ..di import Container
from ..View_Model import Conversion_VM, Response_VM


class Conversion_View:
    @inject
    def All_Possible_Types_DI(c_vm: Conversion_VM.Conversion_VM = Provide(Container.Container.conversions_vm)) -> None:
        Conversion_View.All_Possible_Types(None, c_vm)

    def All_Possible_Types(r_vm: Response_VM.Response_VM, c_vm: Conversion_VM.Conversion_VM) -> None:
        items = c_vm.all_keys()
        print('All the possible conversion types:')
        for from_type in items:
            Conversion_View.List_Specific_From_Types(from_type)
                
    def List_Specific_From_Types(type: str, r_vm: Response_VM.Response_VM, c_vm: Conversion_VM.Conversion_VM) -> None:
        print('From Type: {}'.format(type))
        convertTypes = c_vm.all_to_types(type)
        for to_type in convertTypes:
            obj = c_vm.conversion(type, to_type)
            print('\tCan be converted to Type: {}'.format(to_type))
            print('\tEquation: {}'.format(obj.equation))
            # print('\tID: {}'.format(obj.id))

    def List_By_Conversion_Type(type: str, r_vm: Response_VM.Response_VM, c_vm: Conversion_VM.Conversion_VM):
        pass