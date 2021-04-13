
"""Module for English to Pig Latin translation and supporting methods."""

VOWEL = 'aeiouy'


def is_vowel(letter):
    """Check if a given letter is a vowel.

    :param: str letter
    :return: True if given letter is a vowel, False otherwise
    :rtype: bool

    """
    return letter.lower() in VOWEL


def word_to_pig_latin(word):
    """Change word in english to Pig Latin.

    If the word begins with a consonant move this consonant to the end of the
    word and add 'ay' at the end of the word after the consonant. If the word
    begins with the vowel add 'way' at the end of the word.

    :param: str word
    :return: given word translated to 'Pig Latin' or None if the word is an
    empty string
    :rtype: str or None

    """
    try:
        first_letter = word[0]
    except IndexError:
        print("Word has to have length > 0.")
        return None

    if is_vowel(first_letter):
        return word + 'way'
    return word[1:] + word[0] + 'ay'


def main():
    """Program translating user word to Pig Latin in a loop."""
    while True:
        word = input("Provide word to translate to pig latin: ")
        word_in_pig_latin = word_to_pig_latin(word)

        if word_in_pig_latin is None:
            continue
        print(word_in_pig_latin)

        msg = input("To quit type q to continue press enter.")
        if msg == 'q':
            break


if __name__ == '__main__':
    # Useful to not operate on global namespace
    main()
