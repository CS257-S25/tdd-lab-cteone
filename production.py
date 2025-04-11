import sys


def reverse_word(word):
    new_word = ""
    for letter in word:
        new_word = letter + new_word
    return new_word


def reverse_all_words(phrase):
    words = phrase.split(" ")
    new_words = map(lambda word: reverse_word(word), words)
    return " ".join(new_words)


def main():
    try:
        phrase = sys.argv[1]
        print(reverse_all_words(phrase))
    except IndexError:
        print("Specify phrase")
