from collections import Counter
from itertools import permutations
from Chapter_3.load_dictionary import load

robert_dict_file = load('words.txt')
robert_dict_file = set(robert_dict_file)
solutionsd = set()


def is_word_valid(perm):
    return "".join(perm) in robert_dict_file


def my_perm3(current_words, remaining_letters):
    global solutionsd
    remaining_letters_len = sum(remaining_letters.values())
    if remaining_letters_len == 0:
        # print("current_words:", current_words)
        solutionsd.add(tuple(current_words))
    # elif remaining_letters_len < 2:
    #     return
    for sub_len in range(remaining_letters_len, 1, -1):
        perms = permutations(remaining_letters, sub_len)
        for perm in perms:
            if not is_word_valid(perm):
                continue
            rem = (Counter(remaining_letters) - Counter(perm))
            # print('perm:', perm)
            # print('rem:', rem)
            my_perm3(current_words + [''.join(perm)], rem)


if __name__ == "__main__":
    my_perm3([], Counter('mother'))
    print(solutionsd)
    print(len(solutionsd))
