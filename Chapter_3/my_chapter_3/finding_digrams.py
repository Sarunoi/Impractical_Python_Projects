from collections import Counter
from itertools import permutations
from Chapter_3.load_dictionary import load


def main():
    dictionary = load("words.txt")
    word = 'tmvoordle'.lower()
    word_perms = {''.join(perm) for perm in permutations(word, 2)}
    perms_counter = Counter()

    for entry in dictionary:
        entry = entry.lower()
        if len(entry) <= 1:
            continue

        for word_perm in word_perms:
            perms_counter[word_perm] += entry.count(word_perm)

    print(perms_counter)


if __name__ == '__main__':
    main()