
def clean_dictionary(words_iter, allowed_single_letter_words):
    """Puts words iterable into the list and removes single-letter words from
     it if they're not permitted."""
    cleaned_dictionary = list(words_iter)
    print(cleaned_dictionary)
    for word in cleaned_dictionary:
        print(f"Word: =={word}==")
        if len(word) <= 1 and word not in allowed_single_letter_words:
            cleaned_dictionary.remove(word)
    return cleaned_dictionary


if __name__ == '__main__':
    word_list = ['a', 'b', 'kotek', 'Czarek', 'Róża', 'b', '', 'a', 'konik']
    print(clean_dictionary(word_list, {'a'}))  # interesting problem, '' is not removed
    # https://stackoverflow.com/questions/64842412/why-does-for-loop-exit-for-empty-string-in-python
    for element in list(word_list):
        # print(f"My element {element}")
        pass
