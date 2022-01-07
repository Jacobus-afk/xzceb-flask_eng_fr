
import unittest
from translator import englishToFrench, frenchToEnglish


class testEnglishToFrench(unittest.TestCase):
    def testNullInput(self):
        self.assertRaises(ValueError, englishToFrench, None)
        
    def testTranslation(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

class testFrenchToEnglish(unittest.TestCase):
    def testNullInput(self):
        self.assertRaises(ValueError, frenchToEnglish, None)
        
    def testTranslation(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

unittest.main()