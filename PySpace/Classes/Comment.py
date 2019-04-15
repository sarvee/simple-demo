'''comment class'''

class Comment:
    def __init__(self):
        self.__statusid=None
        self.__comment_text=None
        self.__comment_username=None
        self.__comment_timestamp=None

    def get_statusid(self):
        return self.__statusid


    def get_comment_text(self):
        return self.__comment_text


    def get_comment_username(self):
        return self.__comment_username


    def get_comment_timestamp(self):
        return self.__comment_timestamp


    def set_statusid(self, value):
        self.__statusid = value


    def set_comment_text(self, value):
        self.__comment_text = value


    def set_comment_username(self, value):
        self.__comment_username = value


    def set_comment_timestamp(self, value):
        self.__comment_timestamp = value

