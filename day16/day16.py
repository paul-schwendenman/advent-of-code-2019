import itertools


def find_digit(sequence, pattern_template):
    pattern = itertools.islice(itertools.cycle(pattern_template), 1, None)

    return abs(sum(a * b for a, b in zip(sequence, pattern))) % 10


def calc_pattern(base_pattern, digit_index):
    for item in base_pattern:
        for count in range(digit_index):
            yield item


def fft(sequence, base_pattern=[0, 1, 0, -1]):
    result = []
    for count in range(len(sequence)):
        # result *= 10
        pattern = calc_pattern(base_pattern, count + 1)
        digit = find_digit(sequence, pattern)
        result.append(digit)
        # print(f'appending {digit}: {result}')

    return result


def convert_from_string(string):
    return [int(item) for item in string if item != '\n']


def convert_to_string(array):
    return "".join(str(item) for item in array)


def main():
    with open('input') as input_file:
        data = input_file.read()
    # base_pattern = [0, 1, 0, -1]

    # values = convert_from_string("80871224585914546619083218645595")
    values = convert_from_string(data)

    for step in range(100):
        values = fft(values)
        print(f'step {step}: {convert_to_string(values)}')

    # offset = convert_to_string(values)[:7]
    # print(values[offset:offset+10])
    return convert_to_string(values)[:8]


if __name__ == "__main__":
    print(main())
