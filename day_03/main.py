import math


def read_data(filename):
    data = []
    with open(filename) as f:
        for line in f.read().splitlines():
            data.append([int(x) for x in line])

    return data


def calc_power(data):
    # Calculate gamma and epsilon
    binary_length, line_length = len(data[0]), len(data)
    gamma_list = []
    for i in range(binary_length):
        gamma_list.append(int(line_length / 2 < sum([x[i] for x in data])))
    epsilon_list = [int(not bool(x)) for x in gamma_list]

    # Convert to decimal
    gamma = int(''.join([str(x) for x in gamma_list]), 2)
    epsilon = int(''.join([str(x) for x in epsilon_list]), 2)

    # Return power
    return gamma * epsilon


def calc_life_support(data):
    def filter_data(data_in, index, common=1):
        # Calculate most common value with given index
        value = int(math.ceil(len(data_in)) / 2 <= sum([x[index] for x in data_in]))

        # Take the reverse if least common is required
        value = value if common else not value

        # Filter based on value
        data_filt = [entry for entry in data_in if entry[index] == value]
        return data_filt

    def get_rating(data_in, val):
        common = 1 if val == "oxygen" else 0
        data_filtered, i = data_in, 0
        while len(data_filtered) > 1:
            data_filtered = filter_data(data_filtered, i, common)
            i += 1
        return int(''.join([str(x) for x in data_filtered[0]]), 2)

    # Find ratings
    oxygen = get_rating(data, "oxygen")
    scrubber = get_rating(data, "scrubber")

    return oxygen * scrubber


def main():
    data = read_data("input.txt")
    print(calc_power(data))
    print(calc_life_support(data))


if __name__ == "__main__":
    main()
