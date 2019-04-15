class InvalidStatusException(Exception):
    def __init__(self):
        super().__init__("Can't add Empty Status!")