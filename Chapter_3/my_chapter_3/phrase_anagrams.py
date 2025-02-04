from collections import Counter
import sys

from Chapter_3.load_dictionary import load

dict_file = load('words.txt')


def find_anagrams(name, word_list):
    """Read name and dictionary file and display all anagrams IN name."""
    name_letter_map = Counter(name)
    anagrams = []
    for word in word_list:
        test = ''
        word_letter_map = Counter(word.lower())
        for letter in word:
            if word_letter_map[letter] <= name_letter_map[letter]:
                test += letter
        if Counter(test) == word_letter_map:
            anagrams.append(word)
    print(*anagrams, sep='\n')
    print()
    print(f"Remaining letter = {name}")
    print(f"Number of remaining letters = {len(name)}")
    print(f"Number of remaining (real word) anagrams = {len(anagrams)}")
    return anagrams


def process_choice(name):
    """Check user choice for validity, return choice and leftover letters."""
    while True:
        choice = input(
            "\nMake a choice else Enter to start over or 'q' to end: ")
        if choice == '':
            main()
        elif choice == 'q':
            sys.exit()

        candidate = ''.join(choice.lower().split())
        left_over_list = list(name)
        for letter in candidate:
            if letter in left_over_list:
                left_over_list.remove(letter)
        if len(name) - len(left_over_list) == len(candidate):
            break
        else:
            print("Won't work! Make another choice!", file=sys.stderr)
    name = ''.join(left_over_list)
    return choice, name


def main():
    """Help user build anagram phrase from their name."""

    ini_name = input("Enter name: ")

    name = ''.join(ini_name.lower().split())
    name = name.replace('-', '')
    limit = len(name)
    phrase = ''
    running = True

    while running:
        temp_phrase = phrase.replace(' ', '')
        if len(temp_phrase) < limit:
            print(f"Length of anagram phrase = {len(temp_phrase)}")

            find_anagrams(name, dict_file)
            print("Current anagram phrase =", end=" ")
            print(phrase, file=sys.stderr)

            choice, name = process_choice(name)
            phrase += choice + ' '

        elif len(temp_phrase) == limit:
            print("\n*****FINISHED*****\n")
            print("Anagram of name = ", end="")
            print(phrase, file=sys.stderr)
            print()
            try_again = input(
                "\n\nTry again? (Press Enter else 'q' to quite): ")
            if try_again.lower() == 'q':
                running = False
                sys.exit()
            else:
                main()


if __name__ == '__main__':
    main()
