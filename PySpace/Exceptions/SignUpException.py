
class InvalidUsernameException(Exception):
    def __init__(self):
        super().__init__("Sorry, Username not available")
        
class InvalidPasswordDigitException(Exception):
    def __init__(self):
        super().__init__("Password must contain a digit")
        
class InvalidPasswordSpeacialCharException(Exception):
    def __init__(self):
        super().__init__("Password must contain a special character")
        
class InvalidPasswordLengthException(Exception):
    def __init__(self):
        super().__init__("Password must contain atleast 8 characters")
        
        
class InvalidGenderException(Exception):
    def __init__(self):
        super().__init__("Invalid gender!")
        
class InvalidUsernameOnlyDigitsSpecialCharacterException(Exception):
    def __init__(self):
        super().__init__("user name should contain atleast 1 char")
        
class InvalidNameException(Exception):
    def __init__(self):
        super().__init__("name should not contain any digits or special characters")
        
class InvalidSurnameException(Exception):
    def __init__(self):
        super().__init__("Surname should not contain any digits or special characters")
        
class InvalidCityException(Exception):
    def __init__(self):
        super().__init__("Enter Valid City!")
        
class InvalidRelationshipStatusException(Exception):
    def __init__(self):
        super().__init__("Enter Valid Relationship Status!")
        
class InvalidMobileNumberException(Exception):
    def __init__(self):
        super().__init__("Enter Valid Mobile Number!")
    
class InvalidSecurityKeyException(Exception):
    def __init__(self):
        super().__init__("Enter a Valid Security Word")