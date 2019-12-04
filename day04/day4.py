def has_double_digit(number):
    number = str(number)
    return any([number[counter+1] == digit for counter, digit in enumerate(number[:-1])])


def get_sets(array):
    return [(item, array[counter+1], array[counter+2], array[counter+3]) for counter, item in enumerate(array[:-3])]


def check_four(a, b, c, d):
    return b == c and a != b and c != d


def has_double_digit2(number):
    number = str(number)
    sets = get_sets(number)
    sets.append((None, number[0], number[1], number[2]))
    sets.append((number[3], number[4], number[5], None))

    return any(check_four(a, b, c, d) for a, b, c, d in sets)


def never_decreases(number):
    number = str(number)
    return all([number[counter+1] >= digit for counter, digit in enumerate(number[:-1])])


def main():
    count = sum(1 for number in range(248345, 746315) if has_double_digit2(number) and never_decreases(number))
    print(count)


if __name__ == "__main__":
    main()
