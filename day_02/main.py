def read_data(filename):
    with open(filename) as f:
        data = []
        for line in f.read().splitlines():
            entry = line.split(" ")
            data.append([entry[0], int(entry[1])])

    return data


def calc_pos(data):
    x, y = 0, 0
    for line in data:
        if line[0] == "forward":
            x += line[1]
        elif line[0] == "down":
            y += line[1]
        elif line[0] == "up":
            y -= line[1]

    return x, y


def calc_pos_aim(data):
    x, y, aim = 0, 0, 0
    for line in data:
        if line[0] == "forward":
            x += line[1]
            y += (aim * line[1])
        elif line[0] == "down":
            aim += line[1]
        elif line[0] == "up":
            aim -= line[1]

    return x, y


def main():
    data = read_data("input.txt")
    x, y = calc_pos(data)
    print(x * y)
    x, y = calc_pos_aim(data)
    print(x * y)


if __name__ == "__main__":
    main()
