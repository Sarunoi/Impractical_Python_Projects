from collections import Counter
from Chapter_2.my_chapter_2.load_dictionary import load


def get_letter_distribution(text):
    letter_counter = Counter(text)

    total_letters = sum(letter_counter.values())

    letter_distribution = {
        key: round(100 * value / total_letters, 2)
        for key, value in letter_counter.items()
    }
    return letter_distribution


def main():
    with open('cipher_a.txt') as file:
        testing_string_a = file.read()

    with open('cipher_b.txt') as file:
        testing_string_b = file.read()

    dictionary = load('dictionary.txt')
    dictionary = ''.join(dictionary).upper()

    standard_letter_distribution = get_letter_distribution(dictionary)
    testing_string_a_distribution = get_letter_distribution(testing_string_a)
    testing_string_b_distribution = get_letter_distribution(testing_string_b)
    print(standard_letter_distribution)
    print(testing_string_a_distribution)
    print(testing_string_b_distribution)

    for key, standard_value in standard_letter_distribution.items():
        if key in 'aeiouy'.upper():
            print(f'Letter: {key}, '
                  f'Standard: {standard_value}, '
                  f'Test_A: {testing_string_a_distribution.get(key, 0)}, '
                  f'Test_B: {testing_string_b_distribution.get(key, 0)}')

    abs_diff_a = 0
    abs_diff_b = 0

    for key, standard_value in standard_letter_distribution.items():
        abs_diff_a += abs(standard_value - testing_string_a_distribution.get(key, 0))
        abs_diff_b += abs(standard_value - testing_string_b_distribution.get(key, 0))

    print(f"Diff A: {abs_diff_a}, Diff B: {abs_diff_b}")

    print(f"cipher_a.txt is a {'substitution' if abs_diff_a > 50 else 'transposition'}")
    print(f"cipher_b.txt is a {'substitution' if abs_diff_b > 50 else 'transposition'}")


if __name__ == '__main__':
    main()
    # solution cipher_a.txt is a composition, cipher_b.txt is a transposition
