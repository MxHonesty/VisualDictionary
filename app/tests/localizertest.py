""" Modulul care implementeaza clasa de test pentru Localizer. """

import unittest
from domain import Localizer


class LocalizerTest(unittest.TestCase):
    """ Clasa de test LocalizerTest. """
    def constructor_test(self):
        """ Test pentru constructorul clasei. """
        img = cv2.imread("test_images\\test1.png")
        loc = Localizer(img)
        self.assertEqual(loc.get_min_confidence(), 0)
        
    def test_set_min_confidence(self):
        """ Test pentru setter-ul set_min_confidence. """
        img = cv2.imread("test_images\\test1.png")
        loc = Localizer(img)
        loc.set_min_confidence(100)
        self.assertEqual(loc.get_min_confidence(), 0)
        
if __name__ == "__main__":
    unittest.main()
