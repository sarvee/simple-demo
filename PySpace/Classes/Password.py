'''password class'''

class Password:
    def __init__(self,username):
        self.__username=username
        self.__oldpass1=None
        self.__oldpass2=None
        self.__oldpass3=None

    def get_username(self):
        return self.__username


    def get_oldpass_1(self):
        return self.__oldpass1


    def get_oldpass_2(self):
        return self.__oldpass2


    def get_oldpass_3(self):
        return self.__oldpass3


    def set_username(self, value):
        self.__username = value


    def set_oldpass_1(self, value):
        self.__oldpass1 = value


    def set_oldpass_2(self, value):
        self.__oldpass2 = value


    def set_oldpass_3(self, value):
        self.__oldpass3 = value
