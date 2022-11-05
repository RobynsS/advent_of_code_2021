from day_06.lanterfish import Lanterfish
import copy


def read_data(filename):
    data = []
    with open(filename) as f:
        fish_timers = [int(x) for x in f.read().split(",")]
        for timer in fish_timers:
            data.append(Lanterfish(timer=timer))

    return data


def calc_lanterfish(data, days):
    for i in range(days):
        new_fish = 0
        for fish in data:
            fish.step()
            if fish.has_new():
                new_fish += 1
        data.extend([Lanterfish() for _ in range(new_fish)])

    return len(data)


def calc_lanterfish_opt(data, days):
    breeder_days = [0] * 9
    for fish in data:
        breeder_days[fish.timer] += 1

    for i in range(days):
        index = i % len(breeder_days)
        breeder_days[(index + 7) % len(breeder_days)] += breeder_days[index]

    return sum(breeder_days)


def main():
    data = read_data("input.txt")
    print(calc_lanterfish(copy.deepcopy(data), 80))
    print(calc_lanterfish_opt(copy.deepcopy(data), 256))


if __name__ == "__main__":
    main()
