class PasswordException(Exception):
    def __init__(self):
        super().__init__("This Password is Previously Used")