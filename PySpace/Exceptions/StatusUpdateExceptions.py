class ConfirmationException(Exception):
    def __init__(self):
        super().__init__("only give y/n")