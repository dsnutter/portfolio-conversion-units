
class Functions:
    WHITELIST_EQUATIONS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(', ')', '+', '-', '/', '*', ' ', 'x', '.')

    # this is for security as we are using eval(), we need to sanitize the input for it
    #   in terms of what was passed in since people could shell out to host os and delete a file if we did not
    @staticmethod
    def does_equation_pass_whitelist(input: str):
        sanitized = True
        # if not digits or parens or number operations. x is only possible variable
        for x in input:
            if not (x in Functions.WHITELIST_EQUATIONS):
                sanitized = False
                break
        # if no matching parens
        if input.count('(') != input.count(')'):
            sanitized = False
        return sanitized
    
    @staticmethod
    def is_valid_float(input: str) -> bool:
        try:
            float(input)
            return True
        except ValueError:
            return False
        
    @staticmethod
    def is_valid_string(input) -> bool:
        try:
            temp = str(input)
            if temp.isalnum():
                return True
            return False
        except ValueError:
            return False

    @staticmethod
    def is_valid_filename(input) -> bool:
        try:
            temp = str(input)
            temp = temp.replace(".", "")
            if temp.isalnum():
                return True
            return False
        except ValueError:
            return False

    @staticmethod
    def is_in_list(items: dict) -> bool:
        return items['input'] in items['list']
