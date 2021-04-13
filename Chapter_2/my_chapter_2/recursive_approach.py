
import load_dictionary


def main():
    word_list = load_dictionary.load('words.txt')
    print("Iterate method:")
    pali_list = []
    for entry in word_list:
        if len(entry) > 1 and entry == entry[::-1]:
            pali_list.append(entry)
    print(f"\nNumber of palindromes found = {len(pali_list)}\n")
    print(*pali_list, sep=', ')

    print("\nRecursive method")
    pali_list = []
    for entry in word_list:
        if is_palindrome(entry):
            pali_list.append(entry)
    print(f"\nNumber of palindromes found = {len(pali_list)}\n")
    print(*pali_list, sep=', ')


def is_palindrome(word):
    while True:
        if len(word) <= 1:
            return True
        if not are_edge_chars_the_same(word):
            return False
        word = word[1:-1]  # remove first and last letter


def are_edge_chars_the_same(word):
    return word[0] == word[-1]


if __name__ == '__main__':
    main()
