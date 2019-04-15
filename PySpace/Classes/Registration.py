'''user class'''
class Register:
    def __init__(self):
        self.__user_name=None
        self.__password=None
        self.__name=None
        self.__surname=None
        self.__gender=None
        self.__relationship_status=None
        self.__city=None
        self.__date=None
        self.__mobile_number=None
        self.__security_question=None

    def get_mobile_number(self):
        return self.__mobile_number


    def get_security_question(self):
        return self.__security_question


    def set_mobile_number(self, value):
        self.__mobile_number = value


    def set_security_question(self, value):
        self.__security_question = value


    def get_date(self):
        return self.__date


    def set_date(self, value):
        self.__date = value


    def get_user_name(self):
        return self.__user_name


    def get_password(self):
        return self.__password


    def get_name(self):
        return self.__name


    def get_surname(self):
        return self.__surname


    def get_gender(self):
        return self.__gender


    def get_relationship_status(self):
        return self.__relationship_status


    def get_city(self):
        return self.__city


    def set_user_name(self, value):
        self.__user_name = value


    def set_password(self, value):
        self.__password = value


    def set_name(self, value):
        self.__name = value


    def set_surname(self, value):
        self.__surname = value


    def set_gender(self, value):
        self.__gender = value


    def set_relationship_status(self, value):
        self.__relationship_status = value


    def set_city(self, value):
        self.__city = value
   

   