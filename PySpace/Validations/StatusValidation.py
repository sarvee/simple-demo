import re
from Exceptions import StatusUpdationException


def validate_status(status):
    if(status=='' or status==' ' or status=='  ' or status=='   '):
        raise StatusUpdationException.InvalidStatusException
    else:
        return True