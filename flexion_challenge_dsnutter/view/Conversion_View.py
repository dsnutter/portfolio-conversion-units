from dependency_injector.wiring import Provide, inject
from ..model import Conversions_Many
from ..di import Conversion_Container

# DSN Notes, switch this to be class instead of separate methods?

class Conversion_View:
    @inject
    def All_Possible_Types(many: Conversions_Many.Conversions_Many = Provide(Conversion_Container.Conversion_Container.conversions_many)) -> None:
        items = many.all_from_types
        print('All the possible conversion types:')
        for c in items:
            print('From Type: {}'.format(c))
            convertTypes = many.all_to_types(c)
            for c2 in convertTypes:
                obj = many.conversion(c, c2)
                print('\tCan be converted to Type: {}'.format(c2))
                print('\tEquation: {}'.format(obj.fn))
                

