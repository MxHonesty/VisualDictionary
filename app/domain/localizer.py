""" Modul responsabil pentru implementarea clasei Localizer. """
import pytesseract as pt


class Localizer:
    """ Clasa care se ocupa cu obtinerea textului din imaginea data. """
    def __init__(self, img):
        """img - imaginea: cv2.imread(path)"""    
        pt.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
        self.__results = pt.image_to_data(img, output_type=pt.Output.DICT)
        self.__min_confidence = 0  # increderea minima in rezultat. 
        self.__medie_confidence = self.__determina_media_confidence()

    def set_min_confidence(self, new_min):
        """ Setter pentru atributul __min_confidence. """
        self.__min_confidence = new_min
        
    def get_min_confidence(self):
        """ Getter pentru atributul __min_confidence. """
        return self.__min_confidence
        
    def get_medie_confidence(self):
        """ Getter pentru atributul _medie_confidence. """
        return self.__medie_confidence

    def get_text(self):
        """ Metoda returneaza textul care a fost determinat cu un scor de confidence
            mai mare decat __min_confidence. """
        text_complet = ""
        rez_dict = self.__results
        for i in range(0, len(rez_dict["text"])):
            text = rez_dict["text"][i]
            conf = int(rez_dict["conf"][i])
            if conf > self.__min_confidence:
                text_complet += text + " "
        return text_complet

    def print_rezults(self):
        for i in range(0, len(self.__results["text"])):
            rez_dict = self.__results
            x = rez_dict["left"][i] 
            y = rez_dict["top"][i] 
            w = rez_dict["width"][i] 
            h = rez_dict["height"][i] 

            text = rez_dict["text"][i] 
            conf = int(rez_dict["conf"][i]) 

            # filtru confidence mic 
            if conf > self.__min_confidence:
                print("Confidence: {}".format(conf)) 
                print("Text: {}".format(text)) 
                print("") 
            else:
                print("Could not understand image!")

    def __determina_media_confidence(self):
        """ Functia determina scorul de confidence mediu pentru textul dat. 
            Date de intrare: results, rezultatul metodei image_to_data.
            Date de iesire: media ca float. """
        media = 0
        nr = 0
        for el in self.__results['conf']:
            media += int(el)
            nr += 1
        media /= nr
        return media
