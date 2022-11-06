import statistics


def read_data(filename):
    with open(filename) as f:
        data = [int(x) for x in f.read().split(",")]

    return data


def calc_fuel_constant(data):
    pos = statistics.median(data)
    fuel = 0
    for entry in data:
        fuel += abs(pos - entry)

    return fuel


def dist_to_fuel(distance):
    return distance * (distance + 1) / 2


def calc_fuel_increase(data):
    # Brute force approach
    ans = float('inf')
    for i in range(min(data), max(data)):
        fuel = 0
        for entry in data:
            fuel += dist_to_fuel(abs(i - entry))
        if fuel < ans:
            ans = fuel

    return ans


def main():
    data = read_data("input.txt")
    print(calc_fuel_constant(data))
    print(calc_fuel_increase(data))


if __name__ == "__main__":
    main()
