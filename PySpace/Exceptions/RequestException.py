class InvalidRequestException(Exception):
    def __init__(self):
        super().__init__("Invalid Request")
        
class InvalidSendingRequestException(Exception):
    def __init__(self):
        super().__init__("Request cannot be sent to yourself")
