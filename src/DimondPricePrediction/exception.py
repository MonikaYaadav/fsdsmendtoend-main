import sys

class customexception(Exception):
    def __init__(self,error_message,error_details:sys):
        self.error_message = error_message
        self.error_details = error_details.exc_info()
        super().__init__(*args)

    def __str__(self) -> str:
        return super().__str__()