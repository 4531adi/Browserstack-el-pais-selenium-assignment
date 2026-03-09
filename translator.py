from deep_translator import GoogleTranslator

def translate_titles(titles):

    translated_titles = []

    print("\nTranslated Titles:\n")

    for title in titles:
        translated = GoogleTranslator(source='es', target='en').translate(title)

        print(translated)

        translated_titles.append(translated)

    return translated_titles