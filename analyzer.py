from collections import Counter


def analyze_words(titles):

    words = []

    for title in titles:
        words.extend(title.lower().split())

    counter = Counter(words)

    print("\nRepeated Words (>2 times):\n")

    for word, count in counter.items():
        if count > 2:
            print(word, ":", count)