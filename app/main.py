import cv2
import pytesseract as pt


pt.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
img = cv2.imread("test_images\\test1.png")
img2 = cv2.imread("test_images\\test2.jpg")
img3 = cv2.imread("test_images\\test3.jpg")

text = pt.image_to_string(img)
print(text)

text = pt.image_to_string(img2)
print(text)

text = pt.image_to_string(img3)
print(text)
