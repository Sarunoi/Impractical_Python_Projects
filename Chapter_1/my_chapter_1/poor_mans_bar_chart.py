
"""Module for getting letters distribution of a user string."""

ALPHABET = 'abcdefghijklmnoprstuvwxyz'


def print_letters_distribution(letters_distribution):
    """Print to console letters distribution.

    :param: dict letters_distribution

    """
    for letter, counter in letters_distribution.items():
        print(f"'{letter}': [", end="")
        letter_presence = [letter for _ in range(counter)]
        print(', '.join(letter_presence) + "]")


def get_letters_distribution(text):
    """Get dictionary where keys are letters and values are their count.

    Get dictionary where keys are letters and values are their count in a given
    text.

    :param: str text
    :return: dictionary where keys are from the alphabet and values are their
    count in a given text.
    :rtype: dict

    """
    text.replace(" ", "")
    text.replace("\n", "")

    letters_distribution = {}
    for letter in ALPHABET:
        letters_distribution[letter] = text.count(letter)
    return letters_distribution


def main():
    """Program for displaying letters distribution of a user text."""
    text = input("Provide text which should be processed: ")
    letters_distribution = get_letters_distribution(text)
    print_letters_distribution(letters_distribution)


if __name__ == '__main__':
    main()
