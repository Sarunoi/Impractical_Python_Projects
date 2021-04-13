import random
import time

from Chapter_5.load_dictionary import load


def main():

    # TODO: Should this be package into the class, so the methods don't keep
    #  the state, but the class is?

    # TODO: comparing to the author's solution I again run
    #  into the problem of over complicating. I'm making sure that my names are
    #  random, not just from the top of the list.

    # plain_msg = "Give your word and we rise"
    msg_cleared = ''.join(plain_msg.split()).lower()
    print(msg_cleared)

    print(f"Collection of names has {len(names_collection)} entries")

    dummy_first_name = random.choice(names_collection).lower()
    list_of_names_encrypting_msg = [dummy_first_name]

    letter_on_the_second_position = True

    for letter in msg_cleared:
        if letter_on_the_second_position:
            letter_position = 1
        else:
            letter_position = 2

        list_of_names_encrypting_msg.append(
            choose_name(
                letter, letter_position, list_of_names_encrypting_msg
            )
        )

        letter_on_the_second_position = not letter_on_the_second_position

    print(*list_of_names_encrypting_msg, sep='\n')


def is_name_allowed(name, current_list):
    """Check if name is not already used or not in forbidden names
    collection."""
    forbidden_names = {'Stuart', 'Jacob'}

    return name not in forbidden_names and name not in current_list


def choose_name(letter, letter_position, current_list):
    """Pick a name at random and return if is valid and meets encryption
    criteria."""
    while True:
        name_candidate = random.choice(names_collection)
        if name_candidate[letter_position].lower() != letter:
            continue
        if is_name_allowed(name_candidate, current_list):
            name_candidate = improve_visibility(
                letter_position, name_candidate, True)
            return name_candidate


def improve_visibility(letter_position, name_candidate, update_name):
    """Lower case all the letters in names besides part of the msg that
     is capitalized."""
    if update_name:
        name_candidate = name_candidate.lower()
        name_with_upper_letter = \
            name_candidate[:letter_position] +\
            name_candidate[letter_position].upper() + \
            name_candidate[letter_position+1:]
    else:
        name_with_upper_letter = name_candidate
    return name_with_upper_letter


if __name__ == '__main__':
    plain_msg = "Give your word and we rise"

    names_collection = load("supporters.txt")
    main()
