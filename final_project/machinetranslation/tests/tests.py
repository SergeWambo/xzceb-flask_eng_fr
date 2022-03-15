'''translator unit test module
    test translation functions
'''
import unittest
from translator import french_to_english, english_to_french

class TranslatorTests(unittest.TestCase):
    '''translatorTests unit test class
    '''
    def test_french_to_english_null_input(self):
        '''test the translation of empty input text
            input : ''
            expected: ''
        '''
        self.assertEqual(french_to_english(''),'')
    def test_french_to_english_ok(self):
        '''test the translation of 'Bonjour'
            input : 'Bonjour'
            expected: 'Hello'
        '''
        self.assertEqual(french_to_english('Bonjour'),'Hello')

    def test_french_to_english_ko(self):
        '''test the translation for 'Location' the word exist in english
            input : 'Location'
            expected: not 'Location'
        '''
        self.assertNotEqual(french_to_english('Location'),'Location')

    def test_english_to_french_null_input(self):
        '''test the translation of empty input text
            input : ''
            expected: ''
        '''
        self.assertEqual(english_to_french(''),'')
    def test_english_to_french_ok(self):
        '''test the translation of 'Hello'
            input : 'Hello'
            expected: 'Bonjour'
        '''
        self.assertEqual(english_to_french('Hello'),'Bonjour')
    def test_english_to_french_ko(self):
        '''test the translation for 'Location' the word exist in french
            input : 'Location'
            expected: not 'Location'
        '''
        self.assertNotEqual(english_to_french('Location'),'Location')
if __name__ == '__main__':
    unittest.main()
