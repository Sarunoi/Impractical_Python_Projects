from collections import Counter
import sys
from itertools import permutations
import time
from Chapter_3.load_dictionary import load

dict_file = load('words.txt')
dict_file = dict_file[:int(len(dict_file)*0.1)]
dict_file_counters = {
    word.lower(): Counter(word.lower()) for word in dict_file
}

robert_dict_file = set(dict_file)
solutionsd = set()


def is_word_valid(perm):
    return "".join(perm) in robert_dict_file


def my_perm3(current_words, remaining_letters):
    global solutionsd
    remaining_letters_len = sum(remaining_letters.values())
    if remaining_letters_len == 0:
        # print("current_words:", current_words)
        solutionsd.add(tuple(sorted(current_words)))
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


def get_words_from_letters(
        letters_counter,
        current_solution,
        results,
        word_list_counters=dict_file_counters):

    for word, word_counter in word_list_counters.items():
        solution_with_word = current_solution + ' ' + word
        for letter in word_counter.keys():
            if word_counter[letter] > letters_counter[letter]:
                break
        else:
            remaining_letters = letters_counter - word_counter
            if remaining_letters == Counter():
                results.append(solution_with_word.strip())
            else:
                get_words_from_letters(remaining_letters, solution_with_word, results)
    return results


def main(user_phrase):
    """Help user build anagram phrase from their name."""

    # user_phrase = input("Give a phrase")
    # user_phrase = 'Mother Father Horse'
    # user_phrase = 'mother'
    user_phrase = ''.join(user_phrase.lower().split())
    print(user_phrase)

    results = []

    user_phrase_counter = Counter(user_phrase)

    words_from_name = get_words_from_letters(user_phrase_counter, '', results)

    print(sorted(results))


if __name__ == '__main__':
    user_phrase = 'car'
    start_time = time.time()
    main(user_phrase)
    bs_version_time = time.time() - start_time

    start_time = time.time()
    my_perm3([], Counter(user_phrase))
    # print(sorted(solutionsd))
    rg_version_time = time.time() - start_time
    print(bs_version_time)
    print(rg_version_time)
