""" Modulul care implementeaza clasa de definitie. """

import requests
from errors import DefNotFoundError


class Definitie:
    """ Clasa definitie. """
    def __init__(self, cuvant):
        """ Constructorul primeste un cuvant ca string.
            Raises DefNotFoundError daca nu este gasita definitia cuvantului. """
        self.__cuvant = cuvant
        self.__text = self.__get_definitie()
        
    def get_text(self):
        return self.__text

    def __get_definitie(self):
        """ Salveaza definitia cuvantului in membrul __text. 
            Raises DefNotFoundError daca nu este gasita definitia. """
        r = requests.get("http://localhost:8000/cuvinte/{}/?format=json".format(self.__cuvant))
        text = ""
        try:
            text = r.json()["definitii"][0]["definitie_text"]
        except KeyError:
            text = r.json()["detail"]
            if text == "Not found.":
                raise DefNotFoundError("Cuvantul nu a fost gasit!")
        return text
