"""Program to reverse words in a phrase"""

import sys


def reverse_word(word):
    """Reverses a word"""
    new_word = ""
    for letter in word:
        new_word = letter + new_word
    return new_word


def reverse_all_words(phrase):
    """Reverses each word in a phrase"""
    words = phrase.split(" ")
    new_words = map(reverse_word, words)
    return " ".join(new_words)


def main():
    """Command line usage: takes a phrase as an argument, then prints each word reversed"""
    try:
        phrase = sys.argv[1]
        print(reverse_all_words(phrase))
    except IndexError:
        print("Specify phrase")
