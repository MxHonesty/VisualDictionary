""" Modulul care implementeaza exceptii custom. """


class DefNotFoundError(Exception):
    def __init__(self, erori):
        self.__erori = erori

    def get_erori(self):
        return self.__erori
