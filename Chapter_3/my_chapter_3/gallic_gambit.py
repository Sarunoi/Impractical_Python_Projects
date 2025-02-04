from itertools import permutations
from collections import Counter
from Chapter_3.load_dictionary import load
import sys


VOWELS = 'aeiouy'


def vowel_consonant_word_map(word):
    """Changes any vowel into 'v' and the rest into 'c'."""
    temp_word = ''
    for letter in word:
        if letter in VOWELS:
            temp_word += 'v'
        else:
            temp_word += 'c'
    return temp_word


def prep_words(name, word_list_ini):
    """Prep word list for finding anagrams."""
    print(f'Length initial word_list = {len(word_list_ini)}.')
    len_name = len(name)
    word_list = [
        word.lower() for word in word_list_ini
        if len(word) == len_name
    ]
    print(f"Length of a new word_list = {len(word_list)}")
    return word_list


def cv_map_words(word_list):
    cv_mapped_words = []
    for word in word_list:
        cv_mapped_words.append(vowel_consonant_word_map(word))

    # determine number of UNIQUE c-v patterns
    total = len(set(cv_mapped_words))
    # target fraction to eliminate
    target = 0.05
    # get_number of items in target_fraction
    n = int(total * target)
    count_pruned = Counter(cv_mapped_words).most_common(total - n)
    filtered_cv_map = set()
    for pattern, count in count_pruned:
        filtered_cv_map.add(pattern)
    print(f'Length filtered_cv_maps = {len(filtered_cv_map)}')
    return filtered_cv_map


def cv_map_filter(name, filtered_cv_map):
    """Remove permutations of words based on unlikely cons-vowel combos."""
    perms = {''.join(i) for i in permutations(name)}
    print(f'Length of initial permutation set = {len(perms)}')
    filter_1 = set()
    for candidate in perms:
        if vowel_consonant_word_map(candidate) in filtered_cv_map:
            filter_1.add(candidate)
    print(f"# choices after filter_1 = {len(filter_1)}")
    return filter_1


def trigram_filter(filter_1, trigrams_filtered):
    """Remove unlikely trigrams from permutations."""
    filtered = set()
    for candidate in filter_1:
        for triplet in trigrams_filtered:
            triplet = triplet.lower()
            if triplet in candidate:
                filtered.add(candidate)
    filter_2 = filter_1 - filtered
    print(f'# of choices after filter_2 = {len(filter_2)}')
    return filter_2


def letter_pair_filter(filter_2):
    """Remove unlikely letter-pairs from permutations."""
    filtered = set()
    rejects = {
        'dt', 'lr', 'md', 'ml', 'mr', 'mt', 'mv',
        'td', 'tv', 'vd', 'vl', 'vm', 'vr', 'vt'
    }
    first_pair_rejects = {
        'ld', 'lm', 'lt', 'lv', 'rd',
        'rl', 'rm', 'rt', 'rv', 'tl', 'tm'
    }
    for candidate in filter_2:
        for r in rejects:
            if r in candidate:
                filtered.add(candidate)
        for fp in first_pair_rejects:
            if candidate.startswith(fp):
                filtered.add(candidate)
    filter_3 = filter_2 - filtered
    print(f'# of choices after filter_3 = {len(filter_3)}')
    if 'voldemort' in filter_3:
        print("Voldemort found!", file=sys.stderr)
    return filter_3


def view_by_letter(name, filter_3):
    """Filter to anagrams starting with input letter."""
    print(f"Remaining letters = {name}")
    first = input("Select a starting letter or press Enter To see all:")
    subset = []
    for candidate in filter_3:
        if candidate.startswith(first):
            subset.append(candidate)
    print(*sorted(subset), sep='\n')
    print(f"Number of choices starting with {first} = {len(subset)}")
    try_again = input("Try again? (Press Enter else any other key to Exit):")
    if try_again.lower() == '':
        view_by_letter(name, filter_3)
    else:
        sys.exit()


def main():
    name = 'tmvoordle'.lower()

    word_list_ini = load('words.txt')
    trigrams_filtered = load('least-likely_trigrams.txt')

    word_list = prep_words(name, word_list_ini)
    filtered_cv_map = cv_map_words(word_list)
    filter_1 = cv_map_filter(name, filtered_cv_map)
    filter_2 = trigram_filter(filter_1, trigrams_filtered)
    filter_3 = letter_pair_filter(filter_2)
    view_by_letter(name, filter_3)


if __name__ == '__main__':
    main()
