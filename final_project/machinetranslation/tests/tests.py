import unittest

from translator import english_to_french, french_to_english

class Test_english_to_french(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(english_to_french('Hello'),'') # test for null input.
        self.assertEqual(english_to_french('Hello'),'Bonjour') #test for translation of Hello to Bonjour.
        

class Test_french_to_english(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(french_to_english('Bonjour'),'') # test for null input.
        self.assertEqual(french_to_english('Bonjour'),'Hello') #test for translation of Bonjour to Hello.

unittest.main()