
from collections import Counter


def main():
    with open('input') as file:
        data = list(file.read())[:-1]

    print(data)
    dimensions = 25 * 6
    print(f'{len(data)} / {dimensions} = {len(data) / (dimensions)}')

    layers = [data[i:i+dimensions] for i in range(0, len(data), dimensions)]

    print(layers[0])
    print(len(layers[0]))

    counters = [Counter(layer) for layer in layers]

    num_zeros = 200
    best_index = None

    for index, counter in enumerate(counters):
        if num_zeros > counter['0']:
            num_zeros = counter['0']
            best_index = index

    answer = counters[best_index]

    print(answer['1'] * answer['2'])


def main2():
    with open('input') as file:
        data = list(file.read())[:-1]

    dimensions = 25 * 6

    layers = [data[i:i+dimensions] for i in range(0, len(data), dimensions)]

    image = ['2'] * 150

    for layer in layers:
        for index, pixel in enumerate(layer):
            if image[index] == '2':
                image[index] = pixel
            else:
                pass

    image_rows = [image[i:i+25] for i in range(0, len(image), 25)]

    for row in image_rows:
        for pixel in row:
            if pixel == '0':
                print(' ', end='')
            else:
                print('#', end='')
        print('')


if __name__ == "__main__":
    # main()
    main2()
