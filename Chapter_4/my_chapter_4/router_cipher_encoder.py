
import random

substitue_words = {
    'batteries': 'hounds',
    'vicksburg': 'odor',
    'april': 'clayton',
    '16': 'sweet',
    'grand': 'tree',
    'gulf': 'owl',
    'forts': 'bailey',
    'river': 'hickory',
    '25': 'multiply',
    '29': 'add',
    'admiral': 'hermes',
    'porter': 'langford'
}

original_msg = 'We will run the batteries at Vicksburg the night of April 16 ' \
              'and proceed to Grand Gulf where we will reduce the forts. ' \
              'Be prepared to cross the river on April 25 or 29. ' \
              'Admiral Porter.'

dummy_words = [
    'koala',
    'konik',
    'autobus',
    'czarny',
    'jedziec',
    'samochod',
    'karawana'
]


def get_msg_with_substitue_words(msg, words_dictionary):
    substitue_msg = msg.upper()
    for word, substitue_word in words_dictionary.items():
        substitue_msg = substitue_msg.replace(word.upper(), substitue_word.upper())
    return substitue_msg


def main():
    # print(original_msg)
    substitue_msg = get_msg_with_substitue_words(original_msg, substitue_words)
    print(substitue_msg)

    msg_splited = list(substitue_msg.split())
    # print(cipherlist)

    cols = 6
    rows = 7

    signs_keys = [-1, 3, -2, 6, 5, -4]
    translation_matrix = build_matrix(signs_keys, msg_splited, cols, rows-1)
    print("Translation matrix:")
    print(translation_matrix)
    matrix_with_dummy_words = add_dummy_words(translation_matrix)
    print("Translation matrix with dummy words:")
    print(matrix_with_dummy_words)
    encoded_msg = ''.join(translate_matrix_to_word_list(matrix_with_dummy_words))
    print("Plaintext = {}".format(encoded_msg))


def translate_matrix_to_word_list(matrix):
    word_list = []
    print()
    for column_id in range(len(matrix[0])):
        # print(matrix[0])
        for row_id in range(len(matrix)):
            # print(matrix[row_id])
            # print(column_id, row_id)
            word_list.append(matrix[row_id][column_id])

    return word_list


def add_dummy_words(matrix):
    matrix_with_dummy_words = matrix
    dummy_row = random.choices(dummy_words, k=len(matrix[0]))
    matrix_with_dummy_words.append(dummy_row)
    return matrix_with_dummy_words


def build_matrix(key_int, word_list, cols, rows):
    """Turn every n-items in a list into a new item in a list of lists."""
    translation_matrix = [None] * rows

    for key in key_int:
        fragment = []
        for word_id in range(abs(key), len(word_list), cols):
            fragment.append(word_list[word_id])
        print(fragment)
        if key < 0:  # read bottom-to-top of column
            row_items = fragment
        elif key > 0:  # read top-to-bottom of columnn
            row_items = list((reversed(fragment)))
        translation_matrix[abs(key) - 1] = row_items
    return translation_matrix


if __name__ == '__main__':
    main()
