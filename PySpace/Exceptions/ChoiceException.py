
class InvalidChoiceException(Exception):
    def __init__(self):
        super().__init__("Invalid Choice!!!")
        
class InvalidAutoChoiceException(Exception):
    def __init__(self,message):
        super().__init__(message)