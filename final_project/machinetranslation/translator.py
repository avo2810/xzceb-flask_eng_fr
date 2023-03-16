"""Module translator provide translation between English and French."""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


# Instance of IBM Watson Language
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-08-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """English to French."""
    #write the code here
    global frenchText
    frenchText = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    frenchText = frenchText.get("translations")[0].get("translation")
    return frenchText

def french_to_english(french_text):
    """French to English."""
    #write the code here
    global englishText
    englishText = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    englishText = englishText.get("translations")[0].get("translation")
    return englishText
