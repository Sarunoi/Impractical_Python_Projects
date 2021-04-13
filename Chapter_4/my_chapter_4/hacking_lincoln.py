
ciphertext = 'THIS OFF DETAINED ASCERTAIN WAYLAND CORRESPONDENTS OF AT' \
             ' WHY AND IF FILLS IT YOU GET THEY NEPTUNE THE TRIBUNE ' \
             'PLEASE ARE THEM CAN UP'


def main():
    """Run program and print decrypted plaintext."""

    cipherlist = list(ciphertext.split())

    combinations = get_possible_row_column_combinations(len(cipherlist))

    for comb in combinations:
        cols, rows = comb
        for starting_sign in ['+', '-']:
            print(f'Try cols x rows: {cols} x {rows} with starting sign "{starting_sign}"')
            signs_keys = generate_signs_key(cols, starting_sign)
            translation_matrix = build_matrix(signs_keys, cipherlist, cols, rows)
            plaintext = decrypt(translation_matrix, rows)
            print("Plaintext = {}".format(plaintext))


def generate_signs_key(columns, starting_sign='-'):
    signs_key = []
    if starting_sign == '-':
        column_sign = -1
    else:
        column_sign = 1

    for i in range(1, columns + 1):
        signs_key.append(i * column_sign)
        column_sign *= -1
    print(f'Generated key: {signs_key}')
    return signs_key


def get_possible_row_column_combinations(text_length):
    combinations = []
    for i in range(2, text_length):  # range excludes 1-column ciphers
        if text_length % i == 0:
            combinations.append((i, int(text_length/i)))
    return combinations


def build_matrix(key_int, cipherlist, cols, rows):
    """Turn every n-items in a list into a new item in a list of lists."""
    translation_matrix = [None] * cols
    start = 0
    stop = rows
    for k in key_int:
        if k < 0:  # read bottom-to-top of column
            col_items = cipherlist[start:stop]
        elif k > 0:  # read top-to-bottom of columnn
            col_items = list((reversed(cipherlist[start:stop])))
        translation_matrix[abs(k) - 1] = col_items
        start += rows
        stop += rows
    return translation_matrix


def decrypt(translation_matrix, rows):
    """Loop through nested lists popping off last item to a string."""
    plaintext = ''
    for i in range(rows):
        for matrix_col in translation_matrix:
            word = str(matrix_col.pop())
            plaintext += word + ' '
    return plaintext


if __name__ == '__main__':
    main()

# solution :
# CORRESPONDENTS OF THE TRIBUNE WAYLAND AT NEPTUNE PLEASE ASCERTAIN WHY THEY ARE
# DETAINED AND GET THEM OFF IF YOU CAN THIS FILLS IT UP
