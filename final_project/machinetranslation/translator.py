"""watson translator package"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

# load .env file
load_dotenv()

#apikey & url for watson translator
apikey = os.environ['apikey']
url = os.environ['url']

#set Watson translator
authenticator=IAMAuthenticator(apikey)
language_translator=LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)
language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com')
language_translator

def english_to_french(english_text):
    """english to french function"""
    translation_french_text=language_translator.translate(text=english_text,model_id='en-fr').get_result()
    french_text=translation_french_text['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """french to english function"""
    translation_english_text=language_translator.translate(text=french_text,model_id='fr-en').get_result()
    english_text=translation_english_text['translations'][0]['translation']
    return english_text
