
def main():
    exit_msg = 'q'
    columns = 3

    columns_directions = {}
    remaining_columns = set(range(1, columns + 1))

    while len(remaining_columns) > 0:
        print(f"Exit msg is {exit_msg}")
        user_msg = input(
            "Please provide a column number and a direction of reading in the"
            f" format for example: '-1', or '5'. Possible column: {remaining_columns}. "
        )

        if user_msg == exit_msg:
            break

        if not is_valid_msg(user_msg, remaining_columns):
            print("This input is invalid. Please try again.")
            continue

        column_num, reading_direction = parse_user_msg(user_msg)

        columns_directions.update({column_num: reading_direction})
        remaining_columns -= columns_directions.keys()

    print(columns_directions)


def is_valid_msg(msg, valid_columns):
    try:
        int_msg = int(msg)
    except ValueError:
        return False
    return abs(int_msg) in valid_columns


def parse_user_msg(msg):
    int_msg = int(msg)
    column_num = abs(int_msg)
    if int_msg > 0:
        reading_direction = "top_to_bottom"
    else:
        reading_direction = "bottom_to_top"

    return column_num, reading_direction


if __name__ == '__main__':
    main()
