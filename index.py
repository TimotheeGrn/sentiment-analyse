import nltk
from nltk.corpus import stopwords
from textblob import TextBlob
from googletrans import Translator

# Chargement des stopwords pour le prétraitement
stop_words = set(stopwords.words('french'))

def preprocess_text(text):
    # Convertir en minuscules et supprimer la ponctuation
    text = text.lower()
    text = ''.join([char for char in text if char.isalnum() or char.isspace()])

    # Supprimer les stopwords
    words = text.split()
    words = [word for word in words if word not in stop_words]
    text = ' '.join(words)

    return text

def translate_to_english(text, src_lang='auto'):
    translator = Translator()
    translated_text = translator.translate(text, src=src_lang, dest='en')
    return translated_text.text

def detect_sentiment(sentence, language='fr'):
    # Traduire la phrase en anglais si la langue n'est pas l'anglais
    if language != 'en':
        sentence = translate_to_english(sentence, src_lang=language)

    # Prétraiter la phrase
    processed_sentence = preprocess_text(sentence)

    # Analyser le sentiment de la phrase avec le modèle de langage anglais
    analysis = TextBlob(processed_sentence)

    # Vérifier si le sentiment est proche de 0 pour détecter la non compréhension
    if -0.2 <= analysis.sentiment.polarity <= 0.2:
        return None  # Non compris

    # Renvoyer True si le sentiment est positif, sinon False
    return analysis.sentiment.polarity > 0

# Exemple d'utilisation
if __name__ == "__main__":
    user_language = input("Entrez votre langue (fr/en) : ")
    user_input = input("Entrez une phrase : ")

    sentiment = detect_sentiment(user_input, language=user_language)

    if sentiment is None:
        print("Désolé, je n'ai pas compris la phrase.")
    else:
        print("Sentiment positif." if sentiment else "Sentiment négatif.")
  
