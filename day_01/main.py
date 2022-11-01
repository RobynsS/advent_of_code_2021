def count_increases(data, window):
    count = 0
    for i in range(len(data[:-window])):
        prv = sum(data[i:i + window])
        nxt = sum(data[i + 1:i + window + 1])
        if nxt > prv:
            count += 1

    return count


def main():
    with open('input.txt') as f:
        data = [int(x) for x in f.read().splitlines()]

    print(count_increases(data, 1))
    print(count_increases(data, 3))


if __name__ == "__main__":
    main()
