
"""Test module for pig_latin.py."""

import unittest

from Chapter_1.my_chapter_1.pig_latin import word_to_pig_latin


class PigLatinTranslatorTests(unittest.TestCase):

    """Unit tests class for word_to_pig_latin method."""

    def test_translate_word_starting_with_vowel(self):
        """Verify word_to_pig_latin when given word starts with a vowel.

        Verify that word_to_pig_latin method when given word starting with
        a vowel ads 'way' to the end of the word.

        """
        word = 'opos'
        expected = 'oposway'
        observed = word_to_pig_latin(word)
        self.assertEqual(observed, expected)

    def test_translate_word_starting_with_consonant(self):
        """Verify word_to_pig_latin when given word starts with a consonant.

        Verify that word_to_pig_latin method when given word starting with
        a consonant moves first letter to the end of the word and ads 'ay'.

        """
        word = 'pig'
        expected = 'igpay'
        observed = word_to_pig_latin(word)
        self.assertEqual(observed, expected)

    def test_translate_word_being_empty_string(self):
        """Verify word_to_pig_latin when given word is an empty string.

        Verify that word_to_pig_latin method is returning None when given word
        is an empty string.

        """
        word = ''
        expected = None
        observed = word_to_pig_latin(word)
        self.assertEqual(observed, expected)
