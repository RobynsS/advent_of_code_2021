from day_05.geometry import Line
from collections import Counter


def read_data(filename):
    data = []
    with open(filename) as f:
        for line in f.read().splitlines():
            coor = [int(y) for x in line.split("->") for y in x.strip().split(",")]
            data.append(Line.from_coor(coor[0], coor[1], coor[2], coor[3]))

    return data


def calc_points(data, diagonal=False):
    points = []
    for line in data:
        if line.is_horizontal() or line.is_vertical():
            points.extend(line.get_points_hor_ver())
        if diagonal:
            if line.is_diagonal():
                points.extend(line.get_points_diag())

    return points


def main():
    data = read_data("input.txt")

    counts = Counter(calc_points(data))
    counts_diagonal = Counter(calc_points(data, diagonal=True))
    doubles = [value for value, count in counts.items() if count > 1]
    doubles_diagional = [value for value, count in counts_diagonal.items() if count > 1]
    print(len(set(doubles)))
    print(len(set(doubles_diagional)))


if __name__ == "__main__":
    main()
