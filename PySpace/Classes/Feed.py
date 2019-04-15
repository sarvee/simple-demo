'''status class'''

class Status:
    def __init__(self,username,status):
        self.__username=username
        self.__name=None
        self.__status=status
        self.__statusid=None
        self.__likes=None
        self.__dislikes=None
        self.__status_timestamp=None
        self.__comment=None

    def get_comment(self):
        return self.__comment


    def set_comment(self, value):
        self.__comment = value


    def get_status_timestamp(self):
        return self.__status_timestamp


    def set_status_timestamp(self, value):
        self.__status_timestamp = value


    def get_username(self):
        return self.__username


    def get_status(self):
        return self.__status


    def get_statusid(self):
        return self.__statusid


    def get_likes(self):
        return self.__likes


    def get_dislikes(self):
        return self.__dislikes


    def set_username(self, value):
        self.__username = value


    def set_status(self, value):
        self.__status = value


    def set_statusid(self, value):
        self.__statusid = value


    def set_likes(self, value):
        self.__likes = value


    def set_dislikes(self, value):
        self.__dislikes = value
    



