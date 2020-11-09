""" Modulul responsabil pentru testarea recunoasterea caracterelor pentru 
    anumite imagini preselectate. """
    
import unittest
import cv2
import pytesseract as pt
import os 


def strip_output(text):
    text = " ".join(text.split())
    text = text.replace("\n", " ")
    return text


pt.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

class TestOCR(unittest.TestCase):
    """ Clasa de test pentru recunoasterea unor imagini selectate. """
    def test_image1(self):
        img = cv2.imread("test_images\\test1.png")
        text = pt.image_to_string(img)
        self.assertEqual(strip_output(text), "((( BREAKING NEWS )))")
    
    def test_image2(self):
        img = cv2.imread("test_images\\test2.jpg")
        text = pt.image_to_string(img)
        self.assertEqual(strip_output(text), "Link-uri text si imagine in HTML")
            
    def test_image3(self):
        img = cv2.imread("test_images\\test3.jpg")
        text = pt.image_to_string(img)
        self.assertEqual(strip_output(text), "NU STIU CE M-AS FACE FARA TINE")
    
    def test_image4(self):
        img = cv2.imread("test_images\\test4.png")
        text = pt.image_to_string(img)
        self.assertEqual(strip_output(text), "selectonist s. m. (sil. -0-), pl. selectionisti sursa: Ortografic (2002) adaugata de siveco _actiuni =")
        
    def test_image6(self):
        img = cv2.imread("test_images\\test6.png")
        text = pt.image_to_string(img)
        self.assertEqual(strip_output(text), "A testcase is created by subclassing unittest. testcase. The three individual tests are defined with methods whose names start with the letters test. This naming convention informs the test runner about which methods represent tests.")
        
    def test_imagine7(self):
        img = cv2.imread("test_images\\test7.jpg")
        text = pt.image_to_string(img)
        print(strip_output(text))

if __name__ == "__main__":
    unittest.main()
