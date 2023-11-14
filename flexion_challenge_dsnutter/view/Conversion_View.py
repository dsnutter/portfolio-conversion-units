from dependency_injector.wiring import Provide, inject
from ..di import Container
from ..View_Model import Conversion_VM

# DSN Notes, switch this to be class instead of separate methods?

class Conversion_View:
    @inject
    def All_Possible_Types(vm: Conversion_VM.Conversion_VM = Provide(Container.Container.conversions_vm)) -> None:
        items = vm.all_from_types
        print('All the possible conversion types:')
        for c in items:
            print('From Type: {}'.format(c))
            convertTypes = vm.all_to_types(c)
            for c2 in convertTypes:
                obj = vm.conversion(c, c2)
                print('\tCan be converted to Type: {}'.format(c2))
                print('\tEquation: {}'.format(obj.equation))
                print('\tID: {}'.format(obj.id))
                

