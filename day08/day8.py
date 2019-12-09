
from collections import Counter


class Image():
    def __init__(self, width, height, data=None):
        self.width = width
        self.height = height
        if data:
            self.data = data
        else:
            self.data = ['2'] * (width * height)

    def show(self):
        image_rows = [self.data[i:i+self.width] for i in range(0, len(self.data), self.width)]

        for row in image_rows:
            for pixel in row:
                if pixel == '0':
                    print(' ', end='')
                else:
                    print('#', end='')
            print('')


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

    i = Image(data=image, width=25, height=6)
    i.show()


if __name__ == "__main__":
    main()
    main2()
