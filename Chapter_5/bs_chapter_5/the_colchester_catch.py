# msg = "So, the cold tea didn't please the old finicky woman."


def load_text(file_name):
    with open(file_name) as file:
        msg = file.read()
    return msg


def get_nth_letter_of_every_nth_word(plain_txt_msg, n):
    msg_word_list = plain_txt_msg.split()
    solution = ""
    for word_id in range(n - 1, len(msg_word_list), n):
        if len(msg_word_list[word_id]) < n:
            continue
        solution += msg_word_list[word_id][n - 1]
    return solution


def main():
    msg = load_text("colchester_message.txt")
    for n in range(1, 8):
        solution = get_nth_letter_of_every_nth_word(msg, n)
        print(f"{n} :{solution}")


if __name__ == '__main__':
    main()
