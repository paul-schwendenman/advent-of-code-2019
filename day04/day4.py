def has_double_digit(number):
    number = str(number)
    return any([number[counter+1] == digit for counter, digit in enumerate(number[:-1])])


def never_decreases(number):
    number = str(number)
    return all([number[counter+1] >= digit for counter, digit in enumerate(number[:-1])])


def main():
    count = sum(1 for number in range(248345, 746315) if has_double_digit(number) and never_decreases(number))
    print(count)


if __name__ == "__main__":
    main()
