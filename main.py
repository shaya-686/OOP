class Event:
    def __init__(self, name, date, desc):
        self.__name = name
        self.__date = date
        self.__desc = desc

    def get_name(self):
        return self.__name

    def get_date(self):
        return self.__date

    def get_desc(self):
        return self.__desc

    def set_date(self, new_date):
        self.__date = new_date

    def set_desc(self, new_desc):
        self.__desc = new_desc

    def __str__(self):
        return f"Name: {self.__name}, date: {self.__date}, desc: {self.__desc}"


