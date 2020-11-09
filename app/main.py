import cv2
import pytesseract as pt
from domain.localizer import Localizer

img = cv2.imread("tests\\test_images\\test7.jpg")
loc = Localizer(img)

loc.set_min_confidence(50)
print("Conf min = " + str(loc.get_min_confidence()))
print("Conf medie = " + str(loc.get_medie_confidence()))
print("==============================")
print("Text = " + loc.get_text())
