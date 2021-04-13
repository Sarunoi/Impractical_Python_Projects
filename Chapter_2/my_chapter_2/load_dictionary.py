import sys

"""Module for loading a text file as a list."""


def load(file):
    """Open a text file and return a list of lowercase strings.

    :param: str file
    :return: list of lowercase strings from a given file
    :rtype: list

    """
    try:
        with open(file) as in_file:
            loaded_text = in_file.read().strip().split('\n')
            loaded_text = {x.lower() for x in loaded_text}
            return loaded_text
    except IOError as e:
        print(
            f"{e}\nError opening {file}. Terminating program.",
            file=sys.stderr)
        sys.exit(1)
