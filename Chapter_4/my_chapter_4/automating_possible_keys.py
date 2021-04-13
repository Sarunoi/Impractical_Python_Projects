from itertools import product, permutations


def main():
    # num_of_cols = int(input("Provide number of columns:"))

    num_of_cols = 3

    cols = range(1, num_of_cols + 1)
    cols_wariants = {(col_num, -col_num) for col_num in cols}
    # print(cols_wariants)

    cols_with_direction_perms = product(*cols_wariants)
    # print(list(cols_with_direction_perms))
    # TODO: A problem, uncommenting this breaks the script

    cols_with_direction_order_perms = []
    for col_with_direction_perm in cols_with_direction_perms:
        # print(col_with_direction_perm)
        all_order_perms = permutations(col_with_direction_perm, len(col_with_direction_perm))
        cols_with_direction_order_perms += all_order_perms

    print(sorted(cols_with_direction_order_perms))
    print(len(cols_with_direction_order_perms))


if __name__ == '__main__':
    main()
