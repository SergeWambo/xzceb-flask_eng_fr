''' translator module
     denine functions to translate text from english to french and from french to english
        returns the translated text
'''
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
my_language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

my_language_translator.set_service_url(url)

def english_to_french(english_text):
    ''' Function that translates an english text to french
        Takes the text as parameter
        returns the translated text if text not empty and '' if the text is empty
    '''
    if english_text != '':
        translate_response = my_language_translator.translate(
            text=english_text,model_id='en-fr').get_result()
        translate_response = json.loads(
            json.dumps(translate_response, indent=2, ensure_ascii=False))
        french_text = translate_response["translations"][0]["translation"]
    else :
        french_text = ''

    return french_text


def french_to_english(french_text):
    ''' Function that translates an english text to french
        Takes the text as parameter
        returns the translated text if text not empty and '' if the text is empty
    '''
    if french_text != '':
        translate_response = my_language_translator.translate(
            text=french_text,model_id='fr-en').get_result()
        translate_response = json.loads(
            json.dumps(translate_response, indent=2, ensure_ascii=False))
        english_text = translate_response["translations"][0]["translation"]
    else:
        english_text = ''
    return english_text
