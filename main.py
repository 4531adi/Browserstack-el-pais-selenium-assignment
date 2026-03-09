from scraper import get_articles
from translator import translate_titles
from analyzer import analyze_words


def main():

    spanish_titles = get_articles()

    translated_titles = translate_titles(spanish_titles)

    analyze_words(translated_titles)


if __name__ == "__main__":
    main()