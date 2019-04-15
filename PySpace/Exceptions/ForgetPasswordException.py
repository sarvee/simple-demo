
class InvalidForgetPasswordDetailsException1(Exception):
    def __init__(self):
        super().__init__("Invalid Username")
        
class InvalidForgetPasswordDetailsException2(Exception):
    def __init__(self):
        super().__init__("Entered Username is correct but the Mobile Number is invalid")
        
class InvalidForgetPasswordDetailsException3(Exception):
    def __init__(self):
        super().__init__("Security Answer Doesn't Match")