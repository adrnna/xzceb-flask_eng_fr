#import json
"""Module creating a translator"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """This method will translate english text to french text"""
    french_response = language_translator.translate(english_text, model_id='en-fr').get_result()
    french_text = french_response['translations'][0]['translation']
    #print(json.dumps(french_text, indent=2, ensure_ascii=False))
    return french_text

def french_to_english(french_text):
    """This method will translate french text to english text"""
    english_response = language_translator.translate(french_text, model_id='fr-en').get_result()
    english_text = english_response['translations'][0]['translation']
    #print(json.dumps(english_text, indent=2, ensure_ascii=False))
    return english_text
