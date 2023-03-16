# import translator
import unittest

from translator import english_to_french,french_to_english
class TestTranslator(unittest.TestCase):

    def test_null(self):
        self.assertNotEqual(english_to_french("Hello"), "")
        self.assertNotEqual(french_to_english("Hello"), "")

    def test_englishToFrench(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")


unittest.main()
