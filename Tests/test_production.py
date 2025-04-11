"""module for unit testing methods in production"""

import unittest

from production import reverse_word, reverse_all_words


class TestReverseWord(unittest.TestCase):
    """Tests reverse_word method"""

    def test_reverse(self):
        """Tests a normal string"""
        self.assertEqual(reverse_word("hello"), "olleh", "Reverse word")

    def test_reverse_empty(self):
        """Tests an empty string"""
        self.assertEqual(reverse_word(""), "", "Reverse empty string")


class TestReverseAllWords(unittest.TestCase):
    """Tests reverse_all_words method"""

    def test_reverse(self):
        """Tests a normal phrase"""
        self.assertEqual(
            reverse_all_words("this is a test"), "siht si a tset", "Reverse sentence"
        )

    def test_reverse_empty(self):
        """Tests an empty string"""
        self.assertEqual(reverse_all_words(""), "", "Should be empty")


if __name__ == "__main__":
    unittest.main()
