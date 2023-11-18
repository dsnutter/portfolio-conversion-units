from ..View_Model import Conversion_VM, Response_VM
from .functions import Functions
from ..di.DI_Wireup import DI_Wireup


class View_Functions:

    # generic way of executing a menu chooser an returning true if a predefined choice has been made
    #   it also calls a predefined lambda based on the choice that typically loads another view or performs
    #   some other operation
    #   Note that a 'q' is a hard halt and will exit out of all menus directly to the command prompt
    @staticmethod
    def execute_menu(config: DI_Wireup, title: str, menu_hashmap: dict, 
                     quit_cmd: list, c_vm: Conversion_VM.Conversion_VM, 
                     r_vm: Response_VM.Response_VM):
        print(title)
        for item in menu_hashmap:
            print(f"({item.capitalize()}) {menu_hashmap[item]['text']}")
        choice = ''
        while not choice.isalpha() and choice.lower() not in quit_cmd:
            choice = input("Choose: ")
            choice = choice.lower()
            if choice not in menu_hashmap:
                print("You did not enter a correct choice")
            elif choice not in quit_cmd:
                context = ''
                if 'context' in menu_hashmap[choice]:
                    context = menu_hashmap[choice]['context']
                # lambda options for this is for three vars, a context/type and then appropriate view model
                menu_hashmap[choice]['execute'](context, c_vm, r_vm)
        if choice.lower() in quit_cmd:
            if choice.lower() == 'q':
                config.halt = True
            # false since we dont want to execute the menu any longer
            return False
        else:
            return True

    # possible future, not fully implemented, entering a filename for export to a file
    @staticmethod
    def Enter_Filename(desc: str):
        print(f"Entering a filename for {desc}: ")
        print('Valid charaters are letters and numbers.')
        print('The results will be saved to a CSV file so no need to enter a file extension.')
        print('The path of the file is in the current folder, so no need to enter a path')

        file = ''
        valid = False
        while not valid:
            file = input("My filename is: ")
            valid = Functions.is_valid_string(file)
            if not valid:
                print("Filename entered was not valid, please enter again'")
        return file
