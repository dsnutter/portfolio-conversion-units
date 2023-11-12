
class Functions:
    # this is for security as we are using eval(), we need to sanitize the input for it
    #   in terms of what was passed in since people could shell out to host os and delete a file if we did not
    @staticmethod
    def is_equation_valid(input: str):
        sanitized = True
        # if not digits or parens or number operations. x is only possible variable
        for x in input:
            if not (x.isdigit() or x in ('(', ')', '+', '-', '/', '*', ' ', 'x')):
                sanitized = False
                break
        # if no matching parens
        if input.count('(') != input.count(')'):
            sanitized = False
        return sanitized
