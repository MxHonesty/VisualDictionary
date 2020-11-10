""" Modul care implementeaza clasa de Dictionar."""


class Dictionar:
    """ Clasa care se ocupa de gestionarea cuvintelor din text
        si definitiilor lor. """
    def __init__(self, text):
        """ Constructor primeste ca parmetrii textul formatat. """
        self.__text_complet = text

    def generate_dict(self):
        """ Genereaza un dictionar cu toate cuvintele care au definitie, si
            definitia lor, in ordinea aparitiei. """
        pass

r = requests.get("http://localhost:8000/cuvinte/test/?format=json")
print(r.json())
