
class InvalidpasswordException(Exception):
    def __init__(self):
        super().__init__("Re-enter your password")