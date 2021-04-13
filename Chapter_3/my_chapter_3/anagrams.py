from Chapter_3.load_dictionary import load


def main():
    word_list = load('words.txt')
    stop_program_command = 'q'

    while True:
        user_word = input(
            f"Provide a word or type '{stop_program_command}' to finish: ")

        if user_word == stop_program_command:
            break

        anagrams = get_word_anagrams_from_words_list(user_word, word_list)

        print(anagrams)


def get_word_anagrams_from_words_list(user_word, word_list):
    anagrams = []
    user_word_lowercase = user_word.lower()
    user_word_lowercase_sorted = sorted(user_word_lowercase)
    for word in word_list:
        word_lowercase = word.lower()
        if word_lowercase == user_word_lowercase:
            # Is it better to nest ifs or separate them whenever possible?
            # If change == to != this could be a parent if for the next one
            # for example
            continue
        if sorted(word_lowercase) == user_word_lowercase_sorted:
            anagrams.append(word)
    return anagrams


if __name__ == '__main__':
    main()






