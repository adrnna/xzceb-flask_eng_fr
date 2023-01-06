import unittest
import sys 
sys.path.append('..')
from translator import english_to_french
from translator import french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour') 
    def test2(self): 
        self.assertEqual(english_to_french(0), '0') 
    def test3(self): 
        self.assertEqual(english_to_french('The cat ate my homework.'), 'Le chat a mangé mes devoirs.') 

class TestFrenchToEnglish(unittest.TestCase): 
    def test4(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello') 
    def test5(self): 
        self.assertEqual(french_to_english(0), '0') 
    def test6(self): 
        self.assertEqual(french_to_english("Alors j'ai mangé le chat."), 'So I ate the cat.') 

unittest.main()